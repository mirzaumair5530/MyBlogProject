from django.shortcuts import render, redirect
from .froms import *
from django.contrib import messages
from .models import (RegisterUser, BlogPost, upload_to, Comment)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .search import PostSearch
from .decorators import *
from .customFilters import register
from django.contrib.auth.models import Group


# @login_required(login_url='signin')
@register.filter(name='show')
def show(value, *args, **kwargs):
    return value[:value]


def index(request):
    search = PostSearch()
    posts = BlogPost.objects.all()
    if request.method == "POST":
        search = PostSearch(request.POST, queryset=posts)
        print(search)
        posts = search.qs
        print(posts)
        for i in posts:
            print(i.postHeader)

    context = {
        'posts': posts,
        "search": search
    }

    return render(request, 'homepage.html', context=context)


def about(request):
    data = {
        'title': "About",
        'pagename': "About Page"
    }
    return render(request, 'ComingSoonTemplates/ComingSoon1.html', context=data)


def contact(request):
    data = {
        'title': "Contact",
        'pagename': "Contact Page"
    }
    return render(request, 'ComingSoonTemplates/ComingSoon1.html', context=data)


def notification(request):
    data = {
        'title': "Notification",
        'pagename': "Notification Page"
    }
    return render(request, 'ComingSoonTemplates/ComingSoon1.html', context=data)


def readMore(request):
    pass


@login_required(login_url='signin')
def uploadPost(request):
    if request.user.is_superuser:
        form = postDate(initial={'postAdmin': request.user})
        if request.method == "POST":
            form = postDate(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                messages.success(request, 'Post has been successfully submitted.')

        data = {
            'title': 'uploadPost',
            'form': form
        }
        return render(request, 'UploadPost.html', context=data)
    else:
        return redirect('index')


@is_loggedin
def signin(request):
    form = Signin()
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            userdata = authenticate(request, username=email, password=password)
            if userdata is not None:
                login(request, userdata)
                return redirect('index')
            else:
                messages.error(request, 'Email or password is not correct.')
                return redirect(signin)

    data = {
        'signinForm': form,
        'Title': "Signin",
    }
    return render(request, 'SignIn_SignUp/Signin.html', context=data)


def logoutuser(request):
    logout(request)
    return redirect(signin)


@is_loggedin
def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            group = Group.objects.get(name="User_Group")
            user = RegisterUser.objects.create_user(username=email.split('@')[0], password=password, email=email,
                                                    first_name=fname, last_name=lname)
            user.groups.add(group)

            messages.success(request, 'User has been Successfully registered.')
            return redirect(signup)
    data = {
        'signupForm': form,
        'Title': "SignUp",
    }
    return render(request, 'SignIn_SignUp/Signup.html', context=data)


def viewPost(request, pk):
    post = BlogPost.objects.get(pk=pk)
    commentForm = postComment(initial={"comment_post": post,
                                       "commenter": request.user, })
    comments = post.comment_set.all()

    if request.method == "POST":
        commentForm = postComment(request.POST, )
        commentForm.user = request.user
        if commentForm.is_valid():
            commentForm.save()

    context = {
        'post': post,
        'cform': commentForm,
        'comments': comments,
    }
    return render(request, 'blog-post.html', context)


def passwordForget(request):
    form = resetPassword()

    if request.method == 'POST':
        form = resetPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return redirect('password_reset_done')
    data = {
        'title': 'Reset Password',
        'form': form,
    }
    return render(request, 'passwordForget/passwordForget.html', context=data)


@login_required(login_url='signin')
def profile(request):
    fname = request.user.first_name
    lname = request.user.last_name
    user = RegisterUser.objects.get(email=request.user.email)
    userForm = profileUpdate(initial={'last_name': lname,
                                      "first_name": fname})
    # userForm = profileUpdate(initial=)
    if request.method == "POST":
        userForm = profileUpdate(request.POST, request.FILES)
        if userForm.is_valid():

            user.last_name = userForm.cleaned_data['last_name']
            user.first_name = userForm.cleaned_data['first_name']
            if userForm.cleaned_data['profileImage']:
                user.profileImage = userForm.cleaned_data['profileImage']
            user.save()

    return render(request, template_name='SignIn_SignUp/profile.html', context={'user': userForm, })
