from django.shortcuts import render,HttpResponse,redirect
from django import http
from django.contrib.auth.decorators import login_required
from owner.forms import *
from markdown import markdown
from django.http.response import Http404, HttpResponseNotFound
from django.http import request
import os

@login_required
def home(request):
    posts=Post.objects.filter(created_by=request.user)
    for p in posts:
        p.body=markdown(p.body)
    return render(request,'staff_home.html',{'data':posts})

@login_required
def new_post(request):
    if request.method == "GET":
        pcf=PostCreationForm()
        return render(request, 'staff_post_creation.html', {'form': pcf}) 
    
    pcf = PostCreationForm(request.POST,request.FILES)
    if pcf.is_valid():
        post=pcf.save(commit=False)
        post.created_by=request.user
        post.save()
        return redirect("staff_home")
    return render(request, 'staff_post_creation.html', {'form': pcf})

@login_required
def post_delete(request,id):
    try:
        post=Post.objects.get(pk=id,created_by=request.user)
        if post.featured_image:
            if os.path.isfile(post.featured_image.path):
                os.remove(post.featured_image.path)
        post.delete()
        return redirect('staff_home')
    except:
        return HttpResponseNotFound

#editing the post

@login_required
def post_edit(request,id):
    post=Post.objects.get(pk=id,created_by=request.user)
    if request.method=="GET":
        pcf=PostCreationForm(instance=post)
        return render(request,"staff_post_edit.html",{'form':pcf})
    pcf=PostCreationForm(data=request.POST,instance=post,files=request.FILES)
    if pcf.is_valid():
        pcf.save()
        return redirect('staff_home')
    return render(request, 'staff_post_edit.html', {'form': pcf})

