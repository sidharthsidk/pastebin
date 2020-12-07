from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponseNotFound,HttpResponseBadRequest
from owner.models import Post
from django.http import request
from markdown import markdown
from accounts.views import login

def home(request):
    posts=Post.objects.all().order_by('-created_on')[:6]
    return render(request, 'user_home.html',{'data':posts})

def viewpost(request, url):
    try:
        post = Post.objects.get(slug=url)
        post.body = markdown(post.body)
        return render(request, 'user_view_post.html', {'data': post})
    except:
        return HttpResponseNotFound() 

def search(request):
    search = request.GET.get('s')
    if search:
        posts = Post.objects.filter(title__contains = search).order_by('-created_on')[:50]
        return render(request, 'user_home.html', {'data': posts})
    return HttpResponseBadRequest()