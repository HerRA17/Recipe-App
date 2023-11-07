from django.urls import path
from .views import home, RecipesListView, RecipesDetailView, records

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipesListView.as_view(), name='list'),
    path('list/<pk>', RecipesDetailView.as_view(), name='detail'),
    path('search/', records, name='search')
]