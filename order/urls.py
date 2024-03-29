from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('orderapi', views.OrderViewSet, basename='order')
router.register('orderapirelated', views.OrderViewSetRelated, basename='orderrelated')
router.register('orderdetailapi', views.OrderDetailViewSet, basename='orderdetail')
router.register('orderdetailapirelated', views.OrderDetailViewSetRelated, basename='orderdetailrelated')
router.register('orderserialapi', views.OrderSerialViewSet, basename='orderserial')
router.register('invoiceapi', views.InvoiceViewSet, basename='invoice')
router.register('orderpackagedetailapi', views.OrderPackageDetailViewSet, basename='orderpackagedetail')

urlpatterns = [
    path('', include(router.urls)),
]