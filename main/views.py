from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index_view(request):
    context = {
        'new': News.objects.last(),
        'news': News.objects.all().order_by('-id')[1:3],
        'news_b': News.objects.all().order_by('-id')[3:5],
        'category': Category.objects.all(),
        'd_miss': News.objects.all().order_by('-id')[5:8]

    }

    return render(request,'index.html',context)

def search_view(request):
    title = request.GET.get('search')
    context={
        's_news': News.objects.filter(title__icontains=title),
        'category': Category.objects.all(),
    }
    return  render(request,'search.html',context)


def about_view(request):

    context={
        'about': Aout_us.objects.last(),
        'our_teams': Our_teams.objects.all().order_by('-id')[:4],
         'category': Category.objects.all(),
    }
    return render(request,'about-us.html',context)

def contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Adress.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('contact_url'),

    context = {
        'category': Category.objects.all(),
    }
    return render(request,'contact.html')


def category_view(request,pk):
    category = Category.objects.get(pk=pk)
    context ={
        'category_news': News.objects.filter(category=category),
        'category': Category.objects.all(),
    }
    return render(request,'catagory.html',context)

def single_view(request, pk):
    new = News.objects.get(pk=pk),
    context = {
        'new': new,
        'category': Category.objects.all(),
    }
    return render(request,'single-post.html',context)

def create_blog_view(request):
    if request.method == "POST":
        title = request.method.POST['title']
        img = request.method.Files.get('img')
        category = request.method.POST['category']
        date = request.method.POST['date']
        text = request.method.POST['text']
        News.objects.create(
            title=title,
            category_id=category,
            text=text,
            img=img,
            data=data,
        )
        return redirect('index_url')
        context={
            'category': Category.objects.all(),
        }
    return render(request,'blog-create.html',context)

def update_blog_view(request, pk ):
    new = News.objects.get(pk=pk)
    if request.method == "POST":
        title = request.method.POST['title']
        img = request.method.Files.get('img')
        category = request.method.POST['category']
        date = request.method.POST['date']
        text = request.method.POST['text']
        new.title = title
        new.category_id = category
        new.date = date
        new.text = text
        if  img is not None:
            new.save()
            return redirect('single_url',new.id)
        context ={
            'new': new,
            'category': Category.objects.all(),
        }
        return  render(request,'update-blog.html',context)


def delete_view(request, pk):
    new= News.objects.get(pk=pk)
    new.delete()
    return redirect('index_url')