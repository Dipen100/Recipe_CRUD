from django.db import models

class Recipe(models.Model):
    BREAKFAST = 'breakfast'
    DINNER = 'dinner'
    SALAD = 'salad'
    SNACK ='snack'
    LUNCH = 'lunch'
    DRINK = 'drink'
    VEGETERIAN = 'vegeterian'
    RECIPE_TYPES = [
        (BREAKFAST, 'Breakfast'),
        (DINNER, 'Dinner'),
        (SALAD, 'Salad'),
        (SNACK, 'Snack'),
        (LUNCH, 'Lunch'),
        (DRINK, 'Drink'),
        (VEGETERIAN, 'Vegeterian'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Date Created')
    recipe_type = models.CharField(max_length=20, choices=RECIPE_TYPES)

