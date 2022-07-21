"""fashionstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fashionapi import views
from posts import views as pviews
from products import views as prodviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', views.HelloWorldView.as_view()),
    path('goodmorning', views.GoodmorningView.as_view()),
    path('greetings/',views.GreetingsView.as_view()),
    path('operation/cube/',views.CubeView.as_view()),
    path('operation/fact/',views.FactorialView.as_view()),
    path('operation/fact1/',views.FactorialViewNew.as_view()),
    path('wordcount/',views.WordCountView.as_view()),
    path('social/posts/',pviews.PostView.as_view()),
    path('social/posts/<int:pid>/',pviews.PostDetailView.as_view()),
    path('products/',prodviews.ProductsView.as_view()),
    path('products/<int:pid>',prodviews.ProductDetailView.as_view()),
    path('social/posts/likes/<int:pid>/',pviews.AddLikeView.as_view()),


]
