from celery import shared_task

from NewsPaper.celery import app


@shared_task
def send_mails():
    print('Hello from background task!')
