from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('connectionapi', views.ConnectionViewSet, basename='connection')
router.register('connectionapirelated', views.ConnectionViewSetRelated, basename='connectionrelated')

urlpatterns = [
    path('', include(router.urls)),
]