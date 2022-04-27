from NewsPaper.celery import app


@app.task
def send_mails():
    print('Hello from background task!')
