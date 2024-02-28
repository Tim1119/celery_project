from django.urls import path
from  .views import send_mail_to_all
urlpatterns = [
    path('',send_mail_to_all,name='send_mail'),
]
