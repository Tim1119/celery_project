from django.shortcuts import render,HttpResponse
from .tasks import send_mail_func

# Create your views here.
def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Email Sent')