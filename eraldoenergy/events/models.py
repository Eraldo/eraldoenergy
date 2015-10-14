from django.db import models

__author__ = "Eraldo Helal"


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    type = models.CharField(max_length=50, blank=True)

    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start", "-name"]

    def __str__(self):
        return self.name

    def has_url(self):
        return bool(self.url)
    has_url.boolean = True
