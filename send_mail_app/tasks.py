from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from celery_project import settings
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_mail_func(self):
    try:
        users= User.objects.all()
        for user in users:
            message='This is a test mail practising celery & django'
            mail_subject = 'Hi! Celery testing'
            print('-------->',user.email)
            to_email=user.email
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                # fail_silently=True
                fail_silently=False
            )
    except Exception as e:
        logger.error(f"An error occurred while sending email: {e}")
        raise self.retry(exc=e)  # Retry the task in case of failure

    return 'Done'
