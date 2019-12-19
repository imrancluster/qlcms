from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.utils.http import urlencode


def get_custom_paginator(filter_object, request, limit):

    paginator = Paginator(filter_object, limit)

    try:
        data = paginator.page(request.GET.get('page', 1))
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return data

def my_reverse(viewname, kwargs=None, query_kwargs=None):
    """
    Custom reverse to add a query string after the url
    Example usage:
    url = my_reverse('my_test_url', kwargs={'pk': object.id}, query_kwargs={'next': reverse('home')})
    """
    url = reverse(viewname, kwargs=kwargs)

    if query_kwargs:
        return u'%s?%s' % (url, urlencode(query_kwargs))

    return url