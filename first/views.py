from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .models import Portfolio, Comment
from .forms import BlogPost
# Create your views here.

def index(request):
    blogs = Blog.objects
    portfolios = Portfolio.objects
    return render(request, 'index.html', {'blogs': blogs, 'portfolios': portfolios})

def new(request):
    blogs = Portfolio.objects.all()
    comment = Comment.objects.all()
    return render(request, 'new.html', {'blogs':blogs, 'comment':comment})

def create(request):
    if request.method == "POST":
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('new')
    else:
        form = NewBlog()
        return render(request, 'create.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Portfolio, pk = pk)
    form = NewBlog(request.POST, request.FILES, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('new')
    return render(request, 'create.html', {'form':form})

def delete(request,pk):
    blog = get_object_or_404(Portfolio, pk = pk)
    blog.delete()
    return redirect('new')

def comment(request,post_pk):
    post = get_object_or_404(Portfolio, pk = post_pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid(): #유효성 검사
            comment = form.save(commit=False) #중복저장방지
            comment.post = post #어디 달건지 저장
            comment.save()
            return redirect('new')
    else :
        form = CommentForm()
        return render(request, 'create.html', {'form':form})

def upda(request, post_pk):
    pos = get_object_or_404(Comment, pk = post_pk) #몇번째 댓글 지정

    if request.method =="POST":
        form = CommentForm(request.POST, instance=pos)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('new')
    else :
        form = CommentForm()
        return render(request, 'create.html', {'form':form})

def dele(request, post_pk):
    comment = get_object_or_404(Comment, pk = post_pk)
    comment.delete()
    return redirect('new')
        

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})