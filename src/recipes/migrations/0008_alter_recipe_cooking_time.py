# Generated by Django 4.2.6 on 2023-11-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_id_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.FloatField(),
        ),
    ]