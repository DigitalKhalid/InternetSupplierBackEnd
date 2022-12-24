from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('customerapi', views.CustomerViewSet, basename='customer')
router.register('customerapirelated', views.CustomerViewSetRelated, basename='customerrelated')
router.register('dealerapirelated', views.DealerViewSetRelated, basename='dealerrelated')

urlpatterns = [
    path('', include(router.urls)),
]