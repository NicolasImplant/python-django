from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

posts = [
    {
        'name' : 'Gumball',
        'user' : 'Isabella',
        'Timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://is2-ssl.mzstatic.com/image/thumb/Purple/v4/d3/9c/1f/d39c1f82-2fc3-1b5f-33bc-025174f487cf/source/256x256bb.jpg',
    },

    {
        'name' : 'Cowboy Bebbop',
        'user' : 'Diego',
        'Timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'http://pngwebicons.com/uploads/anime/ico/anime_icon6679.ico',
    },

    {
        'name' : 'Ghost in the shell',
        'user' : 'Nicolás',
        'Timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://styles.redditmedia.com/t5_dxqku/styles/profileIcon_12g7uigwohn71.jpg?width=256&height=256&crop=256:256,smart&s=18557f86cc842f405cb4fcafd91f63facfdc75d7',
    }
]

def list_posts(request):
    """Return a list with existing posts"""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{Timestamp}</i></strong></p>
        <figure><img src='{picture}'/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))