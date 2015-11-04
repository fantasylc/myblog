from django.shortcuts import render
from .models import Song
# Create your views here.


def index(request):
    context = {}
    song_list = Song.objects.all()
    context['song_list'] = song_list
    return render(request, 'music/index.html', context)