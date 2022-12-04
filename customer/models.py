from django.db import models
# from connection.models import Connection
from location.models import SubArea

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='details', verbose_name='User', primary_key=True)
    
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    contact = models.CharField('Contact', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    biography = models.TextField('Biography', blank=True)
    street_address = models.TextField('Steet Address', blank=True)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE, related_name='customers', verbose_name='Sub Area')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        x = f'{self.first_name} {self.last_name}'
        return x

    # def save(self, *args, **kwargs):
    #     is_new = True if not self.id else False
    #     super(self).save(*args, **kwargs)
    #     if is_new:
    #         Connection.objects.create(customer=self.id)

# To create api token automatically when a new user created
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)