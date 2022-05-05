from django.urls import path
from .import views

urlpatterns = [
    path('', views.course, name='course'),
    path('random-password-generator/', views.random_password_generator,
         name='random-password-generator'),
]
