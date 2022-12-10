from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('productapi', views.ProdcutViewSet, basename='product')
router.register('productapirelated', views.ProdcutViewSetRelated, basename='productrelated')
router.register('packagelistapi', views.PackageList, basename='packagelist')

urlpatterns = [
    path('', include(router.urls)),
]