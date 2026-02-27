from django.urls import path

from . import views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('add/', views.add_expense, name='add'),

    path('edit/<int:pk>/', views.edit_expense, name='edit'),

    path('delete/<int:pk>/', views.delete_expense, name='delete'),

]