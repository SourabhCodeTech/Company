from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('html-tutorial-in-hindi/', views.htmlTutorialInHindi,
         name='htmlTutorialInHindi'),
]
