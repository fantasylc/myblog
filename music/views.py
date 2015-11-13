from django.shortcuts import render
from .models import Song
# Create your views here.


def index(request):
    context = {}
    song_istop = Song.objects.filter(is_top=True)
    song_list = Song.objects.filter(is_top=False)
    context['song_list'] = song_list
    context['song_istop'] = song_istop
    return render(request, 'music/index.html', context)
