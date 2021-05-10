"""the_rapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from artist.views_api import ArtistViewSet
from single.view_api import SingleViewSet

router = DefaultRouter()
router.register(r'artist', ArtistViewSet, basename='artist'),
router.register(r'single', SingleViewSet, basename='single')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', ArtistViewSet.artist_list, name='artists_list'),
    path('artist/<int:artistId>', ArtistViewSet.artist_detail, name='artist_update'),
    path('singles/', SingleViewSet.single_list, name='single_list'),
    path('single/save/', SingleViewSet.create_single, name='create_single'),
]
