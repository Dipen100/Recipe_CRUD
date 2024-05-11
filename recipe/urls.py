from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    
    path('list/', views.recipe_list, name='recipe_list'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    
    path('breakfast/', views.breakfast, name='breakfast'),
    path('dinner/', views.dinner, name='dinner'),
    path('add/', views.add_recipe, name='add_recipe'),
]
