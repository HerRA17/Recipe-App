from django.test import TestCase
from django.urls import reverse
from .models import Recipes
# Create your tests here.
class RecipesTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipes.objects.create(name='Tea', ingredients='tea-leaves, water, sugar(optional)', description= 'Add tea-leaves to the bioling water, wait 5 minutes to sit the tea, and add sugar', id= 1, cooking_time= 5)

    def test_recipe_name(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get metadata for the 'name' filed and use it toq uery its data
        field_label = recipe._meta.get_field('name').verbose_name
        # compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get meta data for the recipe_name field and use it to query its max length
        max_length = recipe._meta.get_field('name').max_length
        # compare the value to the expected result
        self.assertEqual(max_length, 50)
    
    def test_recipe_ingredients(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get meta data for the recipe_ingredients field and use it to query its max length
        max_length_ing = recipe._meta.get_field('ingredients').max_length
        # compare the value to the expected result
        self.assertEqual(max_length_ing, 250)
    
    def test_cookingtime_helptext(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get meta data for the recipe_cookingtime field and use it to query the expected text
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        # compare the value to the expected result
        self.assertEqual(recipe_cookingtime, 'in minutes')
    
    def test_description(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # Retrieve the actual description from the database
        recipe_description = recipe.description
        # compare the actual description to the expected result
        expected_description = 'Add tea-leaves to the bioling water, wait 5 minutes to sit the tea, and add sugar'
        self.assertEqual(recipe_description, expected_description)
    
    def test_get_absolute_url(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # compare the value to the expected result
        self.assertEqual(recipe.get_absolute_url(), '/list/1')
        
    
    def test_calculate_difficulty(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # compare the value to the expected result
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')