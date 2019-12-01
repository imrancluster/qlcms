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

from django.contrib.auth.views import LoginView

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
]
