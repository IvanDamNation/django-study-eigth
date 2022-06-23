from datetime import datetime
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from news.models import Category, Post


def news_sender():

    # Get all objects from model 'category'
    for category in Category.objects.all():

        # List for news + paths
        news_from_each_category = []

        # Check week number
        week_number_last = datetime.now().isocalendar()[1] - 1

        # Get pk and place in filter. Also filter with week number
        for news in Post.objects.filter(category_id=category.id,
                                        dateCreation__week=week_number_last).values('pk',
                                                                                    'title',
                                                                                    'dateCreation',
                                                                                    'category_id__name'):
            # Reformat date
            date_format = news.get("dateCreation").strftime("%m/%d/%Y")

            # Make object with field + date + path of news
            new = (f' http://127.0.0.1:8000/news/{news.get("pk")}, {news.get("title")}, '
                   f'Category: {news.get("category_id__name")}, Date creation: {date_format}')

            # Each object place to the list
            news_from_each_category.append(new)
        # Containment for info about subscribers
        subscribers = category.subscribers.all()

        # For testing and debugging
        print('Sending to: ')
        for qaz in subscribers:
            print(qaz.email)

        # Cycle for body (template) of mail to subscribers
        for subscriber in subscribers:
            # Another kind of frontend
            html_content = render_to_string(
                'sender.html', {'user': subscriber,
                                'text': news_from_each_category,
                                'category_name': category.name,
                                'week_number_last': week_number_last})

            msg = EmailMultiAlternatives(
                subject=f'Hello, {subscriber.username}, news of the week in your feed!',
                from_email='fortestapps@yandex.ru',
                to=[subscriber.email]
            )

            msg.attach_alternative(html_content, 'text/html')

            # For testing purposes
            # print(html_content)

            # Uncomment this to work
            msg.send()
