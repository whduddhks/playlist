from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Myplaylist

# Create your views here.

def home(request):
    playlist = Myplaylist.objects.all().order_by('-id')
    playlist = playlist[:3]
    if request.user.is_authenticated:
        my_playlist = Myplaylist.objects.filter(user = request.user)
        return render(request, "home.html", {"playlist":playlist, "my_playlist":my_playlist})
    return render(request, "home.html", {"playlist":playlist})


def detail(request,detail_id):
    detail = get_object_or_404(Myplaylist, pk=detail_id)
    return render(request, "detail.html", {'playlist_detail':detail})


def write(request):
    return render(request, 'write.html')


def create(request):
    new_playlist = Myplaylist()
    new_playlist.title = request.POST["title"]
    new_playlist.writer = request.user.username
    new_playlist.date = timezone.now()
    new_playlist.body = request.POST['body']
    new_playlist.list_type = request.POST['type']
    new_playlist.list_genre = request.POST['genre']
    new_playlist.list_play = request.POST['play']
    new_playlist.list_image = request.FILES['image']
    new_playlist.user = request.user
    new_playlist.save()
    print(request.POST['play'])
    return redirect("/main/detail/" + str(new_playlist.id))


def delete(request,delete_pliatlist_id):
    delete_post = get_object_or_404(Myplaylist, pk=delete_pliatlist_id)
    delete_post.delete()
    return redirect("home")


def edit(request):
    return redirect("home")


def update(request):
    return redirect("home")


def search(request):
    playlist = Myplaylist.objects.all().order_by('-id')
    return render(request, "search.html", {"playlist": playlist})