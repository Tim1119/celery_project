from .tasks import test_func
from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    test_func.delay()
    return HttpResponse('Done')