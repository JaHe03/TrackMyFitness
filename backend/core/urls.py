from django.contrib import admin
from django.urls import path
from apps.accounts.views import CustomUserCreateView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
