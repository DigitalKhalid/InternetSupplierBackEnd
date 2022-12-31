from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('packagesubscriptionapi', views.PackageSubscriptionViewSet, basename='packagesubscription')

urlpatterns = [
    path('', include(router.urls)),
]