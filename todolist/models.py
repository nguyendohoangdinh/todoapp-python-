from __future__ import unicode_literals
from django.utils import timezone
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=250)    #title
    content = models.TextField(blank=True)  #content
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))     #date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))    #date
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title