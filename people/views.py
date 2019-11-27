from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from people.models import Member, UserProfile


class Members(UserPassesTestMixin, TemplateView):
    template_name = 'member/all.html'

    def get_context_data(self, **kwargs):

        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        member_list = Member.objects.filter(branch=branch_id)

        page = self.request.GET.get('page', 1)

        paginator = Paginator(member_list, 1)
        try:
            members = paginator.page(page)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(paginator.num_pages)

        context = super().get_context_data(**kwargs)

        context['members'] = members
        #context['user'] = User.objects.filter(pk=self.request.user)
        return context

    def test_func(self):
        return self.request.user.has_perm('people.view_member')
