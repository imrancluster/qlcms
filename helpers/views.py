from django.shortcuts import render


def error_403(request, exception):
    data = {}
    return render(request, 'errors/error_403.html', data)
