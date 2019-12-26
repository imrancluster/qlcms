from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/index.html')


class Dashboard(UserPassesTestMixin, TemplateView):
    template_name = 'home/dashboard.html'

    def test_func(self):
        return self.request.user.has_perm('people.add_member')
