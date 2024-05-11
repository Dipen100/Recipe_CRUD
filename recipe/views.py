from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def frontpage(request):
    return render(request, 'recipe_types/frontpage.html')
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_actions/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipes = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_actions/recipe_detail.html', {'recipe': recipes})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipes = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipes)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipes)
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('/')
    return render(request, 'recipe_actions/recipe_confirm_delete.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_actions/recipe_form.html', {'form': form})

def breakfast(request):
    breakfast_recipes = Recipe.objects.filter(recipe_type='breakfast')
    return render(request, 'recipe_types/breakfast_recipes.html', {'recipes': breakfast_recipes})

def dinner(request):
    dinner_recipes = Recipe.objects.filter(recipe_type='dinner')
    return render(request, 'recipe_types/dinner_recipes.html', {'recipes': dinner_recipes})