from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse

from people.forms import MemberForm
from people.models import Member, UserProfile


class Members(UserPassesTestMixin, TemplateView):
    template_name = 'member/all.html'

    def get_context_data(self, **kwargs):

        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        member_list = Member.objects.filter(branch=branch_id)

        page = self.request.GET.get('page', 1)

        paginator = Paginator(member_list, 10)
        try:
            members = paginator.page(page)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(paginator.num_pages)

        context = super().get_context_data(**kwargs)

        context['members'] = members
        return context

    def test_func(self):
        return self.request.user.has_perm('people.view_member')


class MemberCreateViews(UserPassesTestMixin, CreateView):
    model = Member
    template_name = 'member/create.html'
    form_class = MemberForm

    def test_func(self):
        return self.request.user.has_perm('people.add_member')

    def form_valid(self, form):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        form.save(branch_id)
        return super(MemberCreateViews, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("members")

