from django.db import models


class Ingredients(models.Model):
    title = models.CharField(max_length=100, verbose_name='Ingredient')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Recipe')
    photo = models.ImageField('Photo', upload_to='photo/', default='default.png')
    ingredients = models.ManyToManyField(Ingredients, verbose_name='Ingredients')
    cooking = models.TextField(verbose_name='Cooking method')
    time_cook = models.TimeField(verbose_name='Cooking time')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
