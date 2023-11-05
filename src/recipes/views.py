from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
# from django.contrib.auth.mixin import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipesListView(ListView): # LoginRequiredMixin within the ()
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(DetailView): # LoginRequiredMixin within the ()
    model = Recipes
    template_name = 'recipes/detail.html'