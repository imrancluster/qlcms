from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django import forms
from django.urls import reverse

from events.filters import ProgramFilter
from events.forms import ProgramForm
from events.models import Program
from people.models import UserProfile, Member


class Programs(UserPassesTestMixin, TemplateView):
    template_name = 'events/all.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        program_list = Program.objects.filter(branch=branch_id).order_by('-pk')

        # Django Filter
        program_filter = ProgramFilter(self.request.GET, queryset=program_list)

        page = self.request.GET.get('page', 1)

        paginator = Paginator(program_filter.qs, 5)
        try:
            programs = paginator.page(page)
        except PageNotAnInteger:
            programs = paginator.page(1)
        except EmptyPage:
            programs = paginator.page(paginator.num_pages)

        context = super().get_context_data(**kwargs)

        # programs with filtering, programs.form.as_p will work
        context['programs'] = programs
        context['filter'] = program_filter
        return context

    def test_func(self):
        return self.request.user.has_perm('events.view_program')


class ProgramCreateViews(UserPassesTestMixin, CreateView):
    model = Program
    template_name = 'events/create.html'
    form_class = ProgramForm

    def form_valid(self, form):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        form.save(branch_id, self.request.user.pk)
        return super(ProgramCreateViews, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProgramCreateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Add New Program"
        return context

    def get_form_kwargs(self):
        kwargs = super(ProgramCreateViews, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs

    def test_func(self):
        return self.request.user.has_perm('events.add_program')

    def get_success_url(self, *args, **kwargs):
        return reverse("programs")


class ProgramUpdateViews(UserPassesTestMixin, UpdateView):
    model = Program
    template_name = 'events/create.html'
    form_class = ProgramForm

    def get_context_data(self, **kwargs):
        context = super(ProgramUpdateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Update Program"
        return context

    def get_form_kwargs(self):
        kwargs = super(ProgramUpdateViews, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs

    def test_func(self):
        return self.request.user.has_perm('events.change_program')

    def get_success_url(self, *args, **kwargs):
        return reverse("programs")


class ProgramDeleteViews(UserPassesTestMixin, DeleteView):
    model = Program
    template_name = 'events/delete.html'

    def test_func(self):
        return self.request.user.has_perm('events.delete_program')

    def get_success_url(self, *args, **kwargs):
        return reverse("programs")


class ProgramDetailViews(UserPassesTestMixin, DetailView):
    model = Program
    template_name = 'events/show.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        context = super(ProgramDetailViews, self).get_context_data(**kwargs)
        context['members'] = Member.objects.filter(branch_id=branch_id)

        attended = []
        member_attended = Program.objects.get(id=self.kwargs.get('pk')).members.all()
        for member in member_attended:
            attended.append(member.id)

        context['member_attended'] = attended

        return context

    def test_func(self):
        return self.request.user.has_perm('events.view_program')


def handle_program_attendance(request: HttpRequest):
    program_id = None
    if request.method == "POST":

        member_ids = request.POST.getlist('attendance')
        program_id = request.POST['program_id']
        program = Program.objects.get(pk=program_id)

        member_attended = Program.objects.get(id=program_id).members.all()

        # remove previous attendance
        for m in member_attended:
            member = Member.objects.get(pk=m.id)
            program.members.remove(member)

        # add attendance
        for id in member_ids:
            member = Member.objects.get(pk=id)
            program.members.add(member)

    return HttpResponseRedirect(reverse('detail_program', kwargs={'pk':program_id}))