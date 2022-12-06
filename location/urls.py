from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('countryapi', views.CountryViewSet, basename='country')
router.register('countrylistapi', views.CountryList, basename='countrylist')
router.register('cityapi', views.CityViewSet, basename='city')
router.register('citylistapi', views.CityList, basename='citylist')
router.register('cityapirelated', views.CityViewSetRelated, basename='cityrelated')
router.register('areaapi', views.AreaViewSet, basename='area')
router.register('arealistapi', views.AreaList, basename='arealist')
router.register('areaapirelated', views.AreaViewSetRelated, basename='arearelated')
router.register('subareaapi', views.SubAreaViewSet, basename='subarea')
router.register('subarealistapi', views.SubAreaList, basename='subarealist')
router.register('subareaapirelated', views.SubAreaViewSetRelated, basename='subarearelated')

urlpatterns = [
    path('', include(router.urls)),
]