from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import BlogPostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# all posts views
def posts(request):
    posts = Post.objects.all()
    # page_number = request.GET.get('page')
    # post_paginator = Paginator(posts , 12)
    # blog_posts = post_paginator.get_page(page_number)
    context = {
    # 'count':post_paginator.count,
	'posts':posts,
    }
    return render (request, "pages/manage_all_post.html",context)

 
# the single post view
def single_post(request,slug):

    post = get_object_or_404(Post, slug=slug)
    
    return render(request,"admin_pages/admin_single_post.html",{'post':post})


# views for using htmx to add comment without page refresh

@login_required
def add_comment(request, slug):

    user = request.user
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if request.user.is_authenticated and form.is_valid():
           latest_comment = form.save(commit=False)
           latest_comment.post = post
           latest_comment.author = user
           latest_comment.save()

    comments = post.comments.all()
    return render(request,"blog/partials/comment_list.html", {'comments':comments})


@login_required
def admin_add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, )
        if form.is_valid():
            form_data = form.save(commit = False)
            form_data.author = request.user
            form_data.save()
            messages.success(request, 'post added succesfully')
            return redirect('blog:add_post')
        else:
           messages.error(request,'unable to add post')
           form = BlogPostForm()
           context ={
            'form':form,
           }
           return render(request, 'pages/add_post.html',context)
           

    form = BlogPostForm()
    context ={
            'form':form,
           }  
    return render(request, 'pages/add_post.html',context)


@login_required
def admin_edit_post(request, slug):
    if request.method =="POST":
        post = Post.objects.get(slug=slug)
        form = BlogPostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            messages.success(request,"post was edited successfully")
            return redirect('blog:blog_posts')
        else:
           messages.error(request,'something went wrong unable to save form')

    else:
        post = Post.objects.get(slug=slug)
        form = BlogPostForm(instance=post)
        context= {
          'form':form
        }
        return render(request,'admin_pages/admin_edit_post.html',context)



@login_required
def admin_delete_post(request,slug):
    post = get_object_or_404(Post, slug=slug).delete()
    return redirect('blog:blog_posts')



def user_posts(request):
    posts = Post.objects.all().order_by('-date_created')
    page_number = request.GET.get('page')
    post_paginator = Paginator(posts, 1)
    page = post_paginator.get_page(page_number)

    context = {
        'count': post_paginator.count,
        'page': page,
    }

    return render (request, "pages/blog.html",context)


# the single post view
def user_single_post(request,slug):

    post = get_object_or_404(Post, slug=slug)
    
    return render(request,"pages/blog-details.html",{'post':post})
