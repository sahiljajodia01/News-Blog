"""test_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from posts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.posts_list, name="list"),
    url(r'^create/$', views.posts_create, name="create"),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', views.posts_delete, name="delete"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, { 'template_name': 'posts/login.html' } , name="logout"),
]
