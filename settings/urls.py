from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('settingsapi', views.SettingViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]