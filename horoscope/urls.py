from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.index),
    path('type/', views.type),
    path('type/<str:element>/', views.elemental),
    path('<int:sign_number>/', views.sign_info_number),
    path('<str:sign>/', views.sign_info, name='horoscope-name'),
    
]
