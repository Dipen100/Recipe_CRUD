from django.db import models
from django.core.validators import MinValueValidator

class Recipe(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    SALAD = 'Salad'
    SNACK ='Snack'
    DRINK = 'Drink'
    SOUP = 'Soup'
    CHICKEN = 'Chicken'
    VEGETARIAN = 'Vegetarian'
    
    RECIPE_TYPES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SALAD, 'Salad'),
        (SNACK, 'Snack'),
        (DRINK, 'Drink'),
        (SOUP, 'Soup'),
        (CHICKEN, 'Chicken'),
        (VEGETARIAN, 'Vegetarian'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=RECIPE_TYPES)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Date Created')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0.00,
    )
    recipe_type = models.CharField(max_length=20, choices=RECIPE_TYPES)

