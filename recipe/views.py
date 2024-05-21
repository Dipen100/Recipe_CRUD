from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Recipe
from .forms import *

from django.db.models import Q
from django.contrib import messages
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

CATEGORY_URL_MAP = {
    'Breakfast': 'breakfast',
    'Lunch': 'lunch',
    'Dinner': 'dinner',
    'Salad': 'salad',
    'Snack': 'snack',
    'Drink': 'drink',
    'Soup': 'soup',
    'Chicken': 'chicken',
    'Vegetarian': 'vegetarian',
}

@login_required(login_url='login')
def frontpage(request):
    return render(request, 'recipe_types/frontpage.html')
    
def recipe_list(request):
    recipes = Recipe.objects.all()
    search_word = None
    if 'q' in request.GET:
        q = request.GET['q']
        if q.strip():
            search_word = q
            search_recipe = Q(name__icontains=q)
            recipes = Recipe.objects.filter(search_recipe)
    else:
        recipes = Recipe.objects.all()
    
    context={
        'recipes': recipes,
        'total_recipes': len(recipes),
    }
    
    return render(request, 'recipe_actions/recipe_list.html', context)

def recipe_detail(request, pk):
    recipes = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_actions/recipe_detail.html', {'recipe': recipes})

def recipe_create(request):
    if not request.user.is_superuser:
        messages.warning(request, "You do not have permission to create a new recipe.")
        return redirect('recipe_list')
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, "Recipe created successfully!")
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipes = get_object_or_404(Recipe, pk=pk)
    if not request.user.is_superuser:
        messages.warning(request, "You do not have permission to update this recipe.")
        category_url = CATEGORY_URL_MAP.get(recipes.category, 'recipe_detail')
        return redirect(category_url)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipes)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            category_url = CATEGORY_URL_MAP.get(recipes.category, 'recipe_detail')
            return redirect(category_url)
    else:
        form = RecipeForm(instance=recipes)
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def recipe_viewdelete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_actions/recipe_confirm_delete.html', {'recipe': recipe})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if not request.user.is_superuser:
        messages.warning(request, "You do not have permission to delete this recipe.")
        category_url = CATEGORY_URL_MAP.get(recipe.category, 'recipe_detail')
        return redirect(category_url)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        category_url = CATEGORY_URL_MAP.get(recipe.category, 'recipe_detail')
        return redirect(category_url)
    
    return render(request, 'recipe_actions/recipe_confirm_delete.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = RecipeForm()
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def breakfast(request):
    breakfast_recipes = Recipe.objects.filter(recipe_type='Breakfast')
    return render(request, 'recipe_types/breakfast_recipes.html', {'recipes': breakfast_recipes})

def lunch(request):
    lunch_recipes = Recipe.objects.filter(recipe_type='Lunch')
    return render(request, 'recipe_types/lunch_recipes.html', {'recipes': lunch_recipes})

def dinner(request):
    dinner_recipes = Recipe.objects.filter(recipe_type='Dinner')
    return render(request, 'recipe_types/dinner_recipes.html', {'recipes': dinner_recipes})

def salad(request):
    salad_recipes = Recipe.objects.filter(recipe_type='Salad')
    return render(request, 'recipe_types/salad_recipes.html', {'recipes': salad_recipes})

def snack(request):
    snack_recipes = Recipe.objects.filter(recipe_type='Snack')
    return render(request, 'recipe_types/snack_recipes.html', {'recipes': snack_recipes})

def drink(request):
    drinks_recipes = Recipe.objects.filter(recipe_type='Drink')
    return render(request, 'recipe_types/drinks_recipes.html', {'recipes': drinks_recipes})

def soup(request):
    soup_recipes = Recipe.objects.filter(recipe_type='Soup')
    return render(request, 'recipe_types/soup_recipes.html', {'recipes': soup_recipes})

def chicken(request):
    chicken_recipes = Recipe.objects.filter(recipe_type='chicken')
    return render(request, 'recipe_types/chicken_recipes.html', {'recipes': chicken_recipes})

def vegetarian(request):
    vegetarian_recipes = Recipe.objects.filter(recipe_type='Vegetarian')
    return render(request, 'recipe_types/vegetarian_dishes.html', {'recipes': vegetarian_recipes})

def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('frontpage')
    
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
   
def SignupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def LogoutPage(request):
	logout(request)
	return redirect('login')
