from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import requests
import random

from posts.forms import PostForm 
#Utilitiwes
from datetime import datetime
# Create your views here.


@login_required
def list_posts(request): 
    letra=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    url=f'https://gateway.marvel.com:443/v1/public/characters?nameStartsWith={(letra[random.randint(0,len(letra)-1)])}&ts=1&apikey=f99464654a38463641f7054fb14ceac6&hash=c2170ac6676424c911d8a86ec74c1e07'
    print(url)
    response = requests.get(url)
    publicaciones = response.json()['data']['results']
    return render(request,'posts/feed.html',{'posts': publicaciones})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new_post.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile       
        }
    )