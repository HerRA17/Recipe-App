from django.contrib import admin
from .models  import Recipe, Ingredient, Profile
from django.contrib.auth.models import Group, User
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "cooking_time", "calculate_difficulty")

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", )

admin.site.unregister(Group)
class ProfileInline(admin.StackedInline):
    model = Profile

# expand user profile
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

#unregister user
admin.site.unregister(User)

#registeruser & profile
admin.site.register(User, UserAdmin)
