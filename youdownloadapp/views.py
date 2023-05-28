from django.shortcuts import render, redirect
from pytube import YouTube, Playlist
import os
from pathlib import Path

# Create your views here.


def youtubelink(request):
    # if the method we are passing from the form is post
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)

        # to set the video resolution
        stream = video.streams.get_lowest_resolution()
        path_to_download = str(os.path.join(Path.home(), 'Downloads'))
        stream.download()
        print(path_to_download)
        return redirect('/')
    return render(request, 'youtubepage.html')





