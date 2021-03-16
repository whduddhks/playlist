from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Myplaylist, Comment  

# Create your views here.

def home(request):
    playlist = Myplaylist.objects.all().order_by('-like')[:3]
    if request.user.is_authenticated:
        my_playlist = Myplaylist.objects.filter(like_users = request.user).order_by('-like')[:3]
        my_list_num = len(my_playlist)
        return render(request, "home.html", {"playlist":playlist, "my_playlist":my_playlist, "my_list_num":my_list_num})
    return render(request, "home.html", {"playlist":playlist})


def detail(request,detail_id):
    detail = get_object_or_404(Myplaylist, pk = detail_id)
    comments = Comment.objects.filter(point = detail_id)
    return render(request, "detail.html", {'playlist_detail':detail, 'comments':comments})


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
    new_playlist.like = 0
    new_playlist.save()
    print(request.POST['play'])
    return redirect("/main/detail/" + str(new_playlist.id))


def delete(request,delete_pliatlist_id):
    delete_post = get_object_or_404(Myplaylist, pk=delete_pliatlist_id)
    delete_post.delete()
    return redirect("home")


def edit(request, edit_playlist_id):
    edit_playlist = get_object_or_404(Myplaylist, pk=edit_playlist_id)
    return render(request, 'edit.html', {'edit_playlist':edit_playlist})


def update(request, update_playlist_id):
    update_playlist = get_object_or_404(Myplaylist, pk=update_playlist_id)
    update_playlist.title = request.POST["title"]
    update_playlist.writer = request.user.username
    update_playlist.date = timezone.now()
    update_playlistt.body = request.POST['body']
    update_playlist.list_type = request.POST['type']
    update_playlist.list_genre = request.POST['genre']
    update_playlist.list_play = request.POST['play']
    update_playlist.list_image = request.FILES['image']
    update_playlist.save()
    return redirect("/main/detail/" + str(update_playlist.id))


def search(request):
    playlist = Myplaylist.objects.all().order_by('-id')
    return render(request, "search.html", {"playlist": playlist})


def like(request, like_playlist_id):
    like_playlist = get_object_or_404(Myplaylist, pk=like_playlist_id)
    if request.user in like_playlist.like_users.all():
        like_playlist.like_users.remove(request.user)
        like_playlist.like -= 1
    else:
        like_playlist.like_users.add(request.user)
        like_playlist.like += 1
    like_playlist.save()
    return redirect('/main/detail/' + str(like_playlist_id))


def writecomment(request, comment_id):
    comment = Comment()
    comment.writer = request.user.username
    comment.content = request.POST['content']
    comment.point = get_object_or_404(Myplaylist, pk=comment_id)
    comment.save()
    return redirect('/main/detail/' + str(comment_id))