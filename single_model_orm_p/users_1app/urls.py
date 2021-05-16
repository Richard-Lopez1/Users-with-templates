from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-movie', views.add_movie),
    path('delete/<int:movie_id>', views.delete)
]