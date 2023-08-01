from django.db import models
from django.contrib.auth.models import User

class TheList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="thelist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    the_list = models.ForeignKey(TheList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    status = models.BooleanField()

    def __str__(self):
        return self.text

