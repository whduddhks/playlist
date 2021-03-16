from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:detail_id>', views.detail, name="detail"),
    path('write/', views.write, name="write"),
    path('create/', views.create, name="create"),
    path('delete/<int:delete_pliatlist_id>', views.delete, name="delete"),
    path('search/', views.search, name="search"),
    path('like/<int:like_playlist_id>', views.like, name="like"),
    path('edit/<int:edit_playlist_id>', views.edit, name="edit"),
    path('update/<int:update_playlist_id', views.update, name="update"),
]