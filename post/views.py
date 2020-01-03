from django.shortcuts import render , HttpResponse , redirect ,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url = "loginUser")
def addarticle(request):

    form = ArticleForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla kaydedildi.")
        return redirect("index")
    context = {
        "form":form
    }

    return render(request , "addarticle.html", context)

def detail(request , id):
    post = Post.objects.filter(id = id).first()
    context = {
        "post":post
    }
    return render(request,"detail.html",context)
@login_required(login_url = "loginUser")
def update(request,id):

    article = get_object_or_404(Post,id=id)
    form = ArticleForm(request.POST or None , request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.save()

        messages.success(request,"Makale başarıyla Güncellendi.")
        return redirect("index")
    context = {
        "form":form,
    }
    return render(request,"update.html",context)
@login_required(login_url = "loginUser")
def delete(request, id):
    post = get_object_or_404(Post,id=id)

    post.delete()

    messages.success(request,"makale başarıyla silindi")

    return redirect("dashboard")
@login_required(login_url = "loginUser")
def dashboard(request):
    
    posts = Post.objects.filter(author = request.user)

    context = {
        "posts":posts
    }

    return render(request,"dashboard.html",context)

def articles(request):
    posts = Post.objects.all()

    context={
        "posts":posts
    }
    return render(request,"articles.html",context)
@login_required(login_url = "loginUser")
def myarticles(request):
    posts = Post.objects.filter(author = request.user)
    context = {
        "posts":posts
    }
    return render(request,"myarticles.html",context)






