from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredients(models.Model):
    """Model for creating tables with ingredients"""
    TYPE = [
        ('g', 'gm.'),
        ('p', 'pcs.')
    ]

    title = models.CharField(max_length=100, verbose_name='Ingredient', default=None)
    quantity = models.IntegerField()
    type = models.CharField(max_length=20, verbose_name='Type', choices=TYPE, default='g')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Recipes(models.Model):
    """Model for creating tables with recipes"""
    title = models.CharField(max_length=255, verbose_name='Recipe')
    photo = models.ImageField('Photo', upload_to='photo/', default='default.png')
    ingredients = models.ManyToManyField(Ingredients, related_name='Ingredients')
    cooking = models.TextField(verbose_name='Cooking method')
    time_cook = models.CharField(max_length=10, verbose_name='Cooking time')
    slug = models.SlugField(unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator', null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse("recipe_info", kwargs={"recipe_slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['created_at']
