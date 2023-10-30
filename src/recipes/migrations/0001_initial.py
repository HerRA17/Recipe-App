# Generated by Django 4.2.6 on 2023-10-30 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=250)),
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('cooking_time', models.IntegerField()),
                ('difficulty', models.CharField(max_length=20)),
            ],
        ),
    ]
