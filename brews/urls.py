from django.urls import path
from . import views

urlpatterns = [
  path('', views.brew_list, name='brew_list'),
  path('brew/<int:pk>/', views.brew_detail, name='brew_detail'),
  path('brew/<int:pk>/edit/', views.brew_edit, name='brew_edit'),
  path('brew/new', views.brew_new, name='brew_new'),
]

