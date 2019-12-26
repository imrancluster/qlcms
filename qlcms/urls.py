"""qlcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static

from django.contrib.auth.views import LoginView

from events.views import ProgramCreateViews, Programs, ProgramUpdateViews, ProgramDeleteViews, ProgramDetailViews, \
    handle_program_attendance
from matirbank.views import MatirBanks, MatirBankCreateViews, MatirBankUpdateViews, MatirBankDeleteViews, \
    MatirBankDetailViews
from qlcms import settings
from . import views
from people.views import *

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),

    # path('', views.index),
    path('', LoginView.as_view()),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),

    path('accounts/', include("django.contrib.auth.urls")),

    # Members
    path('dashboard/members/', Members.as_view(), name='members'),
    path('dashboard/members/create/', MemberCreateViews.as_view(), name='create_member'),
    path('dashboard/members/update/<int:pk>', MembeUpdateViews.as_view(), name='update_member'),
    path('dashboard/members/delete/<int:pk>', MembeDeleteViews.as_view(), name='delete_member'),
    path('dashboard/members/show/<int:pk>', MemberDetailViews.as_view(), name='detail_member'),


    # Events
    path('dashboard/programs/', Programs.as_view(), name='programs'),
    path('dashboard/programs/create/', ProgramCreateViews.as_view(), name='create_program'),
    path('dashboard/programs/update/<int:pk>', ProgramUpdateViews.as_view(), name='update_program'),
    path('dashboard/programs/delete/<int:pk>', ProgramDeleteViews.as_view(), name='delete_program'),
    path('dashboard/programs/show/<int:pk>', ProgramDetailViews.as_view(), name='detail_program'),
    path('handle-program-attendance/', handle_program_attendance, name='program_attendance'),

    # MatirBank
    path('dashboard/banks/', MatirBanks.as_view(), name='banks'),
    path('dashboard/banks/create/', MatirBankCreateViews.as_view(), name='create_bank'),
    path('dashboard/banks/update/<int:pk>', MatirBankUpdateViews.as_view(), name='update_bank'),
    path('dashboard/banks/delete/<int:pk>', MatirBankDeleteViews.as_view(), name='delete_bank'),
    path('dashboard/banks/show/<int:pk>', MatirBankDetailViews.as_view(), name='detail_bank'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
