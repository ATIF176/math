from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('about/', views.About, name="about"),
    path('contact/', views.Contact, name="contact"),
    path('services/', views.Service, name="services"),
    path('exercises/', views.Exercise, name="exercises"),
    path('mcqs/', views.Mcq, name="mcqs"),
    path('quizes/', views.Quiz, name="quizes"),
]