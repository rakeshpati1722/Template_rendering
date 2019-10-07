from django.urls import path
from app import views

urlpatterns = [
    path('about/', views.About.as_view(),name ='About'),
    path('contact/',views.Contact.as_view(),name='Contact'),
    path('', views.Home.as_view(), name='Home'),
]