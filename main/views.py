from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Myplaylist
from .forms import MyplaylistForm

# Create your views here.

def home(request):
    return render(request, "home.html")


def detail(request,detail_id):
    return render(request, "home.html")


def write(request):
    form = MyplaylistForm()
    return render(request, 'write.html', {'form' : form})


def create(request):
    form = MyplaylistForm(request.POST, request.FILES)
    if form.is_valid():
        new_playlist = form.save(commit=False)
        new_playlist.date = timezone.now
        new_playlist.save()
        return redirect("home.html")
    return redirect("write.html")


def delete(request,delete_blog_id):
     return render(request, "home.html")