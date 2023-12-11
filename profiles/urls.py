from django.urls import path
from profiles import views


urlpatterns = [
    path('user_page/', views.user_page, name='user_page'),
]
