from django.db import models
from django.contrib.auth.models import User
from book.models import Recipes


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    nickname = models.CharField(max_length=150, verbose_name='Nickname')
    email = models.EmailField(verbose_name='Mail', null=True, blank=True)
    avatar = models.ImageField("avatar", default='default.png', upload_to='avatars/')
    favourites = models.ManyToManyField(Recipes, blank=True, default=None, related_name='favourite_recipe')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

