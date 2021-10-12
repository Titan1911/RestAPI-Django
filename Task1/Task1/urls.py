"""Task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from json_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.account,name='account-list'),
    path('account-api', views.accountApi),
    path('account-list',views.accountListAPIView.as_view()),
    path('account-create',views.accountCreateAPIView.as_view()),
    path('account-delete/<str:pk>',views.accountDeleteAPIView.as_view()),
    path('account-detail/<str:pk>',views.accountRetrieveAPIView.as_view()),
    path('account-update/<str:pk>',views.accountUpdateAPIView.as_view()),
]
