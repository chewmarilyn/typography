from django.shortcuts import render


def home(request):
    render(request, 'type/index.html')
