from django.contrib import auth
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.core.paginator import Paginator

from q.forms import *
from .models import *
# Create your views here.

def index(request, page_number=1):
    all_articles = Post.objects.all()
    page = Paginator(all_articles, 3)
    return render(request, 'index.html', {'blog': page.page(page_number), 'username': auth.get_user(request).username})

def detail(request, Post_id):
    comment_form = CommentsForm
    ques = {}
    ques.update(csrf(request))
    ques['blog'] = get_object_or_404(Post, pk=Post_id)
    ques['category'] = Category
    ques['comments'] = Comments.objects.filter(com_posts_id=Post_id)
    ques['form'] = comment_form
    ques['username'] = auth.get_user(request).username
    return render(request, 'detail.html', ques)

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category.html', {'blog': Post.objects.filter(post_cat_id=category_id), 'category':category, 'username': auth.get_user(request).username})


def addlikes(request, Post_id):
    try:
        if Post_id in request.COOKIES:
            return redirect('/{0}'.format(Post_id))
        else:
            artitcl = Post.objects.get(id=Post_id)
            artitcl.post_likes += 1
            artitcl.save()
            # создание куки
            #response = redirect('/{0}'.format(Post_id))
            #response.set_cookie(Post_id, 'test')
            #return response
            return redirect('/{0}'.format(Post_id))
    except ObjectDoesNotExist:
        raise Http404

    return redirect('/{0}'.format(Post_id))


def addcomment(request, Post_id):
    if request.POST and ("pause" not in request.session):
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.FILES:
                comment.ComImage = request.FILES['ComImage']

            comment.user = request.user
            comment.com_posts = Post.objects.get(id=Post_id)
            comment.save()
            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect('/{0}'.format(Post_id))


def addpost(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = AddPost()
    if request.POST:
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if request.FILES:
                post.upload = request.FILES['upload']

            post.user = request.user
            post.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
            return redirect('/')

    return render(request, 'AddPost.html', args)


def regulations(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['regulations'] = Regulations.objects.all()
    return render(request, 'regulations.html', args)

def history(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['histoty'] = History.objects.all()
    return render(request, 'history.html', args)