from celery import shared_task
from accounts.management.commands.runapscheduler import news_sender


@shared_task
def send_mails():
    print('Hello from background task!')


@shared_task
def send_mail_for_sub_every_week():
    news_sender()
