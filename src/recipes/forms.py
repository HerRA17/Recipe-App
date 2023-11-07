from django import forms

CHART_CHOICES = (
        ('#1', 'Bar chart'),
        ('#2', 'Pie chart'),
        ('#3', 'Line chart')
    )

DIFFIC_CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=50)
    ingredients = forms.CharField(max_length=250)
    recipe_diff = forms.ChoiceField(choices=CHART_CHOICES)
    chart_type = forms.ChoiceField(choices=DIFFIC_CHOICES)