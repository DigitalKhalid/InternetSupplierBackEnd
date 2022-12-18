from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('paymentapirelated', views.PaymentViewSetRelated, basename='paymentrelated')
router.register('paymentapi', views.PaymentViewSet, basename='payment')
router.register('paymentinvoiceapi', views.PaymentInvoiceViewSet, basename='paymentinvoice')

urlpatterns = [
    path('', include(router.urls)),
]