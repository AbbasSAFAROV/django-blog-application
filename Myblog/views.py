from django.shortcuts import render , HttpResponse
from post.models import Post
# Create your views here.
def index(request):
    return render(request , "index.html")

def home(request):
    posts = Post.objects.all()

    context={
        "posts":posts
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def sport(request):
    return render(request,"sports.html")