from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from events.filters import ProgramFilter
from events.forms import ProgramForm
from events.models import Program
from people.filters import MemberFilter
from people.models import UserProfile, Member
from events.utils import get_presence_members_by_program_id, get_program_history
from qlcms.utils import get_custom_paginator, my_reverse


class Programs(UserPassesTestMixin, TemplateView):
    template_name = 'events/all.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        program_list = Program.objects.filter(branch=branch_id).order_by('-pk')

        # Django Filter
        program_filter = ProgramFilter(self.request.GET, queryset=program_list)

        context = super().get_context_data(**kwargs)

        # programs with filtering, programs.form.as_p will work
        context['programs'] = get_custom_paginator(program_filter.qs, self.request, 10)
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

        """
            Member search section
            List of all absence members
        """
        member_list = Member.objects.filter(branch=branch_id).order_by('-pk')

        # Django Filter
        member_filter = MemberFilter(self.request.GET, queryset=member_list)
        context['members'] = get_custom_paginator(member_filter.qs, self.request, 5)
        context['filter'] = member_filter

        member_attended = get_presence_members_by_program_id(self.kwargs.get('pk'))
        context['member_attended'] = member_attended

        attended = []
        for member in member_attended:
            attended.append(member.id)
        context['member_attended_ids'] = attended
        context['program_history'] = get_program_history(self.kwargs.get('pk'))
        # context['all_programs'] = Program.get_all_members(self.kwargs.get('pk'))

        return context

    def test_func(self):
        return self.request.user.has_perm('events.view_program')


def handle_program_attendance(request: HttpRequest):
    program_id = None
    if request.method == "POST":
        member_ids = request.POST.getlist('attendance')
        remove_members = request.POST.getlist('remove_members')
        program_id = request.POST['program_id']
        program = Program.objects.get(pk=program_id)

        # member_attended = Program.objects.get(id=program_id).members.all()

        # remove previous attendance
        for id in remove_members:
            member = Member.objects.get(pk=id)
            program.members.remove(member)

        # add attendance
        for id in member_ids:
            member = Member.objects.get(pk=id)
            program.members.add(member)

    return HttpResponseRedirect(
        my_reverse(
            'detail_program',
            kwargs={'pk':program_id},
            query_kwargs={
                'page': request.GET.get('page')
            }
        ))