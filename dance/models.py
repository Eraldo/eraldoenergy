from django.db import models

__author__ = 'eraldo'


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    alias = models.CharField(max_length=50, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    type = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)

    country = models.CharField(max_length=50, blank=True, default="Austria")
    url = models.URLField(blank=True)

    partner = models.OneToOneField("Instructor", blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-order", "name"]

    def __str__(self):
        return self.name

    def has_url(self):
        return bool(self.url)
    has_url.boolean = True

    def save(self, checkPartner=True, *args, **kwargs):
        super(Instructor, self).save()
        if self.partner and checkPartner:
            self.partner.partner = self
            self.partner.save(checkPartner=False)
