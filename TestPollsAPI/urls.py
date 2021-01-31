
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('polls.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
