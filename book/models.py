from django.db import models


class Ingredients(models.Model):
    title = models.CharField(max_length=100, verbose_name='Ingredient', default=None)
    quantity = models.IntegerField()
    type = models.CharField(max_length=20, verbose_name='Type', default=None)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Recipe')
    photo = models.ImageField('Photo', upload_to='photo/', default='default.png')
    ingredients = models.ManyToManyField(Ingredients, related_name='Ingredients')
    cooking = models.TextField(verbose_name='Cooking method')
    time_cook = models.TimeField(verbose_name='Cooking time')
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
