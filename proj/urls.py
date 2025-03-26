from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # User logs in here
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refreshes expired token
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
