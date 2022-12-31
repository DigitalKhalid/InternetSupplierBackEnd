from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from customizations.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('', include('connection.urls')),
    path('', include('location.urls')),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('payment.urls')),
    path('', include('settings.urls')),
    path('', include('package.urls')),

    # path('', include(router.urls)),
    # path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refreshtoken/', TokenRefreshView.as_view(), name='token_refrsh'),
    # path('verifytoken/', TokenRefreshView.as_view(), name='token_Verify'),

    # path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)