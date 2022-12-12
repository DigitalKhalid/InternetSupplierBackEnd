from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('orderapi', views.OrderViewSet, basename='order')
router.register('orderapirelated', views.OrderViewSetRelated, basename='orderrelated')
router.register('orderdetailapi', views.OrderDetailViewSet, basename='orderdetail')

urlpatterns = [
    path('', include(router.urls)),
]