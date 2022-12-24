from django.db import models
from django.contrib.auth.models import User
from location.models import SubArea


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='employees', verbose_name='User', null=True, blank=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    designation = models.CharField('Designation', max_length=20)
    contact = models.CharField('Contact', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    street_address = models.TextField('Steet Address', blank=True)
    # subarea = models.ForeignKey(
    #     SubArea, on_delete=models.CASCADE, related_name='employees', verbose_name='Sub Area')
    date_created = models.DateTimeField('Date Created', auto_now_add=True)
    biography = models.TextField('Biography', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
