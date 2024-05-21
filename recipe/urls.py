from django.urls import path
from . import views

urlpatterns = [
    path('frontpage/', views.frontpage, name='frontpage'),
    
    path('list/', views.recipe_list, name='recipe_list'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/update/', views.recipe_update, name='recipe_update'),
    path('<int:pk>/viewdelete/', views.recipe_viewdelete, name='recipe_viewdelete'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    
    path('breakfast/', views.breakfast, name='breakfast'),
    path('lunch/', views.lunch, name='lunch'),
    path('dinner/', views.dinner, name='dinner'),
    path('salad/', views.salad, name='salad'),
    path('snack', views.snack, name='snack'),
    path('drink', views.drink, name='drink'),
    path('soup', views.soup, name='soup'),
    path('chicken', views.chicken, name='chicken'),
    path('vegetarian', views.vegetarian, name='vegetarian'),
    
    path('add/', views.add_recipe, name='add_recipe'),
    
    path('', views.LoginPage, name='login'),
	path('logout/', views.LogoutPage, name='logout'),
	path('signup/', views.SignupPage, name='signup'),
]
