from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:detail_id>', views.detail, name="detail"),
    path('write/', views.write, name="write"),
    path('create/', views.create, name="create"),
    path('delete/<int:delete_blog_id>', views.delete, name="delete"),
]