from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(subject, massage):
    sleep(10)
    send_mail(subject='celery and rabbit',
              message='test message',
              from_email='admin@zoo.local',
              recipient_list=['valentinakuzmenkova@gmail.com'],
              fail_silently=False)
