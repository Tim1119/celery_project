from django.urls import path
from  .views import send_mail_to_all,schedule_mail
urlpatterns = [
    path('',send_mail_to_all,name='send_mail'),
    path('schedule_mail/',schedule_mail,name='schedule_mail'),
]
