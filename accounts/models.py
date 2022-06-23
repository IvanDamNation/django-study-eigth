from django.db import models
from django.contrib.auth.models import User


class SubscribersToCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey('news.Category', on_delete=models.CASCADE)
