from django.urls import path
from .import views, include

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('menu/', views.menu_view, name = 'menu'),
    path('book/', views.book_view, name = 'book'),
    path('about/', views.about_view, name = 'about')

]