from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    # id = models.PositiveBigIntegerField(primary_key=True)
    cooking_time = models.FloatField(help_text='in minutes')
    description = models.TextField(default='No description available')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 7:
            difficulty = 'Hard'
        return difficulty
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
    
    def _str_(self):
        str(self.name)