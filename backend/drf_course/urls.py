"""drf_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views as core_views
from rest_framework.authtoken.views import obtain_auth_token
from ecommerce import views as ecommerce_views
from users import views as user_view
from rest_framework_simplejwt import views as jwt_views

router=routers.DefaultRouter()

router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

urlpatterns=router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    # path('api-token-auth/',obtain_auth_token),#gives access to auth token,
    path('accounts/register',user_view. RegistrationView.as_view(), name='register'),
    path('accounts/login', user_view.LoginView.as_view(), name='register'),
    path('accounts/logout', user_view.LogoutView.as_view(), name='register'),
    path('accounts/change-password', user_view.ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

 
]
