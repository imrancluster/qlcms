from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from matirbank.filters import MatirBankFilter
from matirbank.forms import MatirBankForm
from matirbank.models import MatirBank
from people.models import UserProfile
from qlcms.utils import get_custom_paginator


class MatirBanks(UserPassesTestMixin, TemplateView):
    template_name = 'matirbank/all.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        matirbank_list = MatirBank.objects.filter(branch=branch_id).order_by('-pk')

        # Django Filter
        matirbank_filter = MatirBankFilter(self.request.GET, queryset=matirbank_list, user=self.request.user, request=self.request)



        context = super().get_context_data(**kwargs)

        # members with filtering, members.form.as_p will work
        context['banks'] = get_custom_paginator(matirbank_filter.qs, self.request, 10)
        context['filter'] = matirbank_filter
        context['form_type'] = 'new-form'
        return context

    def test_func(self):
        return self.request.user.has_perm('matirbank.view_matirbank')

    # def get_filterset_kwargs(self, filterset_class):
    #     kwargs = super(MatirBanks, self).get_filterset_kwargs(filterset_class)
    #     kwargs['user'] = self.request.user
    #     return kwargs




class MatirBankCreateViews(UserPassesTestMixin, CreateView):
    model = MatirBank
    template_name = 'matirbank/create.html'
    form_class = MatirBankForm

    def get_context_data(self, **kwargs):
        context = super(MatirBankCreateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Add new bank"
        return context

    def test_func(self):
        return self.request.user.has_perm('matirbank.add_matirbank')

    def form_valid(self, form):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        form.save(branch_id, self.request.user.pk)
        return super(MatirBankCreateViews, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MatirBankCreateViews, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'formType': 'new'})
        return kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse("banks")


class MatirBankUpdateViews(UserPassesTestMixin, UpdateView):
    # class view will automatically create context = member
    model = MatirBank
    template_name = 'matirbank/create.html'
    form_class = MatirBankForm

    def get_context_data(self, **kwargs):
        context = super(MatirBankUpdateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Update matir bank"
        context['form_type'] = 'update-form'
        return context

    def test_func(self):
        return self.request.user.has_perm('matirbank.change_matirbank')

    def get_form_kwargs(self):
        kwargs = super(MatirBankUpdateViews, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'formType': 'update'})
        return kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse("banks")


class MatirBankDeleteViews(UserPassesTestMixin, DeleteView):
    model = MatirBank
    template_name = 'matirbank/delete.html'

    def test_func(self):
        return self.request.user.has_perm('matirbank.delete_matirbank')

    def get_success_url(self, *args, **kwargs):
        return reverse("banks")
