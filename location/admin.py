from django.contrib import admin
from .models import Country, City, Area, SubArea

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(SubArea)
