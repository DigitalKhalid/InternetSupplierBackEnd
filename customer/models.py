from django.db import models


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='details', verbose_name='User', primary_key=True)
    
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    contact = models.CharField('Contact', max_length=50, blank=True)
    biography = models.TextField('Biography', blank=True)
    steet_address = models.TextField('Steet Address', blank=True)
    area = models.TextField('Area', blank=True)
    city = models.TextField('City', blank=True)
    image = models.ImageField(upload_to='images', default='/images/avatar.jpg')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        x = f'{self.user.firtname} {self.user.lastname}'
        return x


# To create api token automatically when a new user created
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)