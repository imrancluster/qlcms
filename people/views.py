from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from people.filters import MemberFilter, ContactFilter
from people.forms import MemberForm, ContactForm
from people.models import Member, UserProfile, Contact
from qlcms.utils import get_custom_paginator


class Members(UserPassesTestMixin, TemplateView):
    template_name = 'member/all.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        member_list = Member.objects.filter(branch=branch_id).order_by('-pk')

        # Django Filter
        member_filter = MemberFilter(self.request.GET, queryset=member_list)

        context = super().get_context_data(**kwargs)

        # members with filtering, members.form.as_p will work
        context['members'] = get_custom_paginator(member_filter.qs, self.request, 10)
        context['filter'] = member_filter
        context['form_type'] = 'new-form'
        return context

    def test_func(self):
        return self.request.user.has_perm('people.view_member')


class MemberCreateViews(UserPassesTestMixin, CreateView):
    model = Member
    template_name = 'member/create.html'
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MemberCreateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Add new member"
        return context

    def test_func(self):
        return self.request.user.has_perm('people.add_member')

    def form_valid(self, form):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        form.save(branch_id, self.request.user.pk)
        return super(MemberCreateViews, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("members")


class MembeUpdateViews(UserPassesTestMixin, UpdateView):
    # class view will automatically create context = member
    model = Member
    template_name = 'member/create.html'
    form_class = MemberForm

    def get_context_data(self, **kwargs):
        context = super(MembeUpdateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Update Member"
        context['form_type'] = 'update-form'
        return context

    def test_func(self):
        return self.request.user.has_perm('people.change_member')

    def get_success_url(self, *args, **kwargs):
        return reverse("members")


class MembeDeleteViews(UserPassesTestMixin, DeleteView):
    model = Member
    template_name = 'member/delete.html'

    def test_func(self):
        return self.request.user.has_perm('people.delete_member')

    def get_success_url(self, *args, **kwargs):
        return reverse("members")


class MemberDetailViews(UserPassesTestMixin, DetailView):
    model = Member
    template_name = 'member/show.html'

    def get_context_data(self, **kwargs):
        context = super(MemberDetailViews, self).get_context_data(**kwargs)
        member = Member.objects.get(id=self.kwargs.get('pk'))
        context['banks'] = member.matirbank_set.all().order_by('-id')
        return context

    def test_func(self):
        return self.request.user.has_perm('people.view_member')


'''
Member Contacts
'''


class Contacts(UserPassesTestMixin, TemplateView):
    template_name = 'contact/all.html'

    def get_context_data(self, **kwargs):
        branch_id = UserProfile.objects.filter(user=self.request.user)[0].branch.id
        contact_list = Contact.objects.filter(member__branch=branch_id).order_by('-pk')

        # Django Filter
        contact_filter = ContactFilter(self.request.GET, queryset=contact_list)

        context = super().get_context_data(**kwargs)

        # members with filtering, members.form.as_p will work
        context['contacts'] = get_custom_paginator(contact_filter.qs, self.request, 10)
        context['filter'] = contact_filter
        context['form_type'] = 'new-form'
        return context

    def test_func(self):
        return self.request.user.has_perm('people.view_contact')


class ContactCreateViews(UserPassesTestMixin, CreateView):
    model = Contact
    template_name = 'contact/create.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactCreateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Add new contact"
        return context

    def get_form_kwargs(self):
        kwargs = super(ContactCreateViews, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs

    def test_func(self):
        return self.request.user.has_perm('people.add_contact')

    def form_valid(self, form):
        form.save(self.request.user.pk)
        return super(ContactCreateViews, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("contacts")


class ContactUpdateViews(UserPassesTestMixin, UpdateView):
    # class view will automatically create context = member
    model = Contact
    template_name = 'contact/create.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactUpdateViews, self).get_context_data(**kwargs)
        context['view_form_title'] = "Update contact"
        context['form_type'] = 'update-form'
        return context

    def get_form_kwargs(self):
        kwargs = super(ContactUpdateViews, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs

    def test_func(self):
        return self.request.user.has_perm('people.change_contact')

    def get_success_url(self, *args, **kwargs):
        return reverse("contacts")


class ContactDeleteViews(UserPassesTestMixin, DeleteView):
    model = Contact
    template_name = 'contact/delete.html'

    def test_func(self):
        return self.request.user.has_perm('people.delete_contact')

    def get_success_url(self, *args, **kwargs):
        return reverse("contacts")


class ContactDetailViews(UserPassesTestMixin, DetailView):
    model = Contact
    template_name = 'contact/show.html'

    def test_func(self):
        return self.request.user.has_perm('people.view_contact')
