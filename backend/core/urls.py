from django.contrib import admin
from django.urls import path
from apps.accounts.views import CustomUserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', CustomUserCreateView.as_view(), name='register'),
]
