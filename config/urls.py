"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from book import views as book_views
from profiles import views as profiles_views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.index, name='home'),
    path('recipes/', include('book.urls')),
    path('login/', profiles_views.login_user, name='login'),
    path('logout/', profiles_views.logout_user, name='logout'),
    path('register/', profiles_views.register_user, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = book_views.pageNotFound
