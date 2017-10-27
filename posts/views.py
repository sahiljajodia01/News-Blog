from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form
    }
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))

    return render(request, "create.html", context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "detail.html", context)

def posts_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page_request_var = 'Page'

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
        "page_request_var": page_request_var
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
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Item saved")
        return HttpResponseRedirect(instance.get_absolute_url())


    context = {
        "form": form,
        "instance": instance,
        "title": instance.title,
    }

    return render(request, "create.html", context)

def posts_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("list")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()

    context = { 'form': form }
    return render(request, 'signup.html', context)
