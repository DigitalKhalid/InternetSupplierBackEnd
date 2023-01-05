from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('productapi', views.ProdcutViewSet, basename='product')
router.register('productapirelated', views.ProductViewSetRelated, basename='productrelated')
router.register('packagelistapi', views.PackageList, basename='packagelist')
router.register('productlistapi', views.ProductList, basename='productlist')
router.register('catagoryapi', views.CatagoryViewSet, basename='catagory')
router.register('unitapi', views.UnitViewSet, basename='unit')

urlpatterns = [
    path('', include(router.urls)),
]