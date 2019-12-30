from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from matirbank.helper import get_ready_banks


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/index.html')

@csrf_exempt
def ready_banks(request):

    # @TODO: need to check authentication

    if request.is_ajax():
        ready_banks = get_ready_banks(request.user, 30)
        return render(request, 'matirbank/partial/ready_banks.html', context={
            'banks': ready_banks,
            'total_banks': len(ready_banks)
        })


class Dashboard(UserPassesTestMixin, TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['banks'] = []
        context['total_banks'] = 0

        return context

    def test_func(self):
        return self.request.user.has_perm('people.add_member')
