from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Recipes modal
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    id = models.PositiveBigIntegerField(primary_key=True)
    cooking_time = models.FloatField(help_text='in minutes')
    instructions = models.TextField(default='No instructions available')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard')
    ]
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def calculate_difficulty(self):
        num_ingredients = self.ingredients.count()
        if self.cooking_time < 10 and num_ingredients < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and num_ingredients >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and num_ingredients < 7:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'
        return difficulty
    
    def __str__(self):
        return self.name
    
# model for individual Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name="ingredients_used"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ingredients_used"
    )

    def __str__(self):
        return f"{self.ingredient} - {self.recipe}"
# modal Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)