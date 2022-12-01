from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('locationapi', views.LocationViewSet, basename='location')
router.register('countryapi', views.CountryViewSet, basename='country')
router.register('cityapi', views.CityViewSet, basename='city')
router.register('cityapirelated', views.CityViewSetRelated, basename='cityrelated')
router.register('areaapi', views.AreaViewSet, basename='area')
router.register('areaapirelated', views.AreaViewSetRelated, basename='arearelated')
router.register('subareaapi', views.SubAreaViewSet, basename='subarea')

urlpatterns = [
    path('', include(router.urls)),
]