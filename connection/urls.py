from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('connectionapi', views.ConnectionViewSet, basename='connection')

urlpatterns = [
    # path('', views.home, name='home'),
    path('', include(router.urls)),
]