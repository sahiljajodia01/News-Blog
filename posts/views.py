from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Token
from .forms import PostForm
from django.contrib.auth.models import User
from .token import account_activation_token
from django.core.mail import send_mail
from test_blog import settings
from .forms import CustomUserCreationForm, CustomUserLoginForm


def posts_create(request):
    user = request.user
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        post = Post.objects.create(user=request.user.username, image=request.FILES['image'], title=request.POST['title'], content=request.POST['content'])
        post.save()
        # instance = form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        # instance.save()
        # post = Post.objects.get(instance=instance)
        # post.user = request.user
        messages.success(request, "Successfully created")
        return redirect('list')

    context = {
        "form": form,
        "user": user,
    }
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))

    return render(request, "create.html", context)


def posts_detail(request, id):
    user = request.user
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance": instance,
        "user": user,
    }

    return render(request, "detail.html", context)


def posts_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = 'Page'
    logged_in_user = request.user

    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "List",
        "object_list": queryset,
        "page_request_var": page_request_var,
        "user": logged_in_user,
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, 'list.html', context)


def posts_update(request, id):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    user = request.user
    if form.is_valid():
        instance.image = request.FILES['image']
        instance.title = request.POST['title']
        instance.content = request.POST['content']

        # instance = form.save(commit=False)
        instance.save()


        messages.success(request, "Item saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "instance": instance,
        "title": instance.title,
        "user": user,
        }

    return render(request, "create.html", context)


def posts_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("list")


def signup(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)

            subject = "Email verification for django"
            message = account_activation_token.make_token(user)
            token = Token.objects.create(user=user, token=message)
            token.save()
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('verify')
    else:
        form = CustomUserCreationForm()

    context = {'form': form,
               "user": user,
    }
    return render(request, 'signup.html', context)


def verify(request):
    user = request.user
    if request.method == 'POST':
        token = request.POST['token']

        if token == request.user.token.token:
            request.user.valid = True
            print("Valid")
            return redirect('list')
        else:
            print("Invalid")
            return redirect('signup')

    context = {
        "user": user,
    }
    return render(request, 'verification.html', context)


def loguser(request):
    user = request.user
    print("Before request method")
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        print("Before form valid")

        username = request.POST['username']
        password = request.POST['password']
        print("Before authentication")
        user = authenticate(username=username, password=password)
        login(request, user)
        print("After authentication")
        return redirect('list')
    else:
        form = CustomUserLoginForm()

    context = {
        "form": form,
        "user": user,
    }
    return render(request, 'login.html', context)

