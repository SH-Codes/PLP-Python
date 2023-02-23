from django.urls import path
from .import views

urlpatterns = [
    path('home', views.houseListings, name = "home" ),
    path('details/<pk>/', views.retrieveDetails, name = "details"),
]