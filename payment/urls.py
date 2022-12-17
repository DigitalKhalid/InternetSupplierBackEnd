from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('paymentapirelated', views.PaymentViewSetRelated, basename='paymentrelated')
router.register('paymentapi', views.PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]