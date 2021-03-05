from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Myplaylist
from .forms import MyplaylistForm

# Create your views here.

def home(request):
    playlist = Myplaylist.objects.all().order_by('-id')
    playlist = playlist[:3]
    my_playlist = []
    if request.user.is_authenticated:
        my_playlist = Myplaylist.objects.filter(user = request.user)
    return render(request, "home.html", {"playlist":playlist, "my_playlist":my_playlist})


def detail(request,detail_id):
    detail = get_object_or_404(Myplaylist, pk=detail_id)
    return render(request, "detail.html", {'playlist_detail':detail})


def write(request):
    form = MyplaylistForm()
    return render(request, 'write.html', {'form' : form})


def create(request):
    form = MyplaylistForm(request.POST, request.FILES)
    if form.is_valid():
        new_playlist = form.save(commit=False)
        new_playlist.writer = request.user.username
        new_playlist.date = timezone.now
        new_playlist.save()
        return redirect("home.html")
    return redirect("write.html")


def delete(request,delete_pliatlist_id):
    delete_post = get_object_or_404(Blog, pk=delete_pliatlist_id)
    delete_post.delete()
    return render(request, "home.html")