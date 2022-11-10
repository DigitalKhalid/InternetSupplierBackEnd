from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from customer import views

router = DefaultRouter()

router.register('customerapi', views.CustomerViewSet, basename='customer')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)