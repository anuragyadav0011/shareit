from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('register/', views.register),
    path('verify/', views.verify),
    path('login/', views.login),
    path('myadmin/', views.adminhome),
    path('manageusers/', views.manageusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('user/', views.userhome),
    path('sharenotes/', views.sharenotes),
    path('viewnotes/', views.viewnotes),
    path('funds/', views.funds),
    path('payment/', views.payment),
    path('success/', views.success),
    path('cancel/', views.cancel)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
