# Generated by Django 4.2.6 on 2023-12-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_ingredients_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='title',
            field=models.CharField(default=None, max_length=100, verbose_name='Ingredient'),
        ),
    ]