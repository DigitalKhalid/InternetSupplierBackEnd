from django.db import models

class Country(models.Model):
    country = models.CharField('Country', max_length=50)

    def __str__(self):
        return self.country

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities', verbose_name='Country')
    city = models.CharField('city', max_length=50)

    def __str__(self):
        return self.city

class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='areas', verbose_name='City')
    area = models.CharField('Area', max_length=50)

    def __str__(self):
        return self.area

class SubArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='subareas', verbose_name='Area')
    subarea = models.CharField('Sub Area', max_length=50)

    def __str__(self):
        return self.subarea