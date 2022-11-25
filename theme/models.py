from django.db import models
from colorfield.fields import ColorField

class Theme(models.Model):
    title = models.CharField('Theme Title', max_length=50)

    def __str__(self):
        return self.title

class ThemeDetail(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='details', verbose_name='Theme')
    color = ColorField('Text Color', format='hexa')
    field_color = ColorField('Field Text Color', format='hexa')
    border_color = ColorField('Border Color', format='hexa')

    def __str__(self):
        return f'{self.theme} Theme' 
