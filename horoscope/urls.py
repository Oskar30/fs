from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_number>/', views.sign_info_number),
    path('<str:sign>/', views.sign_info, name='horoscope-name'),

]
