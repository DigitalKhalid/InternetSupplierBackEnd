from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('connectionapi', views.ConnectionViewSet, basename='connection')
router.register('connectionlistapi', views.ConnectionListViewSet, basename='connectionlist')
router.register('connectionapirelated', views.ConnectionViewSetRelated, basename='connectionrelated')
router.register('activeexpiredconnectionapi', views.ActiveExpiredConnectionsViewSet, basename='activeexpiredconnections')

urlpatterns = [
    path('', include(router.urls)),
]