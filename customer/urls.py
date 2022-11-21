from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('customerapi', views.CustomerViewSet, basename='customer')

urlpatterns = [
    # path('', views.home, name='home'),
    path('', include(router.urls)),
]
