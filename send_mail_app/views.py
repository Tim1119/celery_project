from django.shortcuts import render,HttpResponse
from .tasks import send_mail_func
from django_celery_beat.models  import PeriodicTask,CrontabSchedule
import json
# Create your views here.
def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Email Sent')

def schedule_mail(request):
    schedule , created = CrontabSchedule.objects.get_or_create(hour=2,minute=24)
    tasks = PeriodicTask.objects.create(crontab=schedule,name='schedule_mail_tasks_for staffs'+str(schedule.id),task='send_mail_app.tasks.send_mail_func')
    # you can pass args but you have to add the args to the tasks.py in the app
    return HttpResponse('Created & Scheduled mail automatically')