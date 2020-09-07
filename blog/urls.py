from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloghome, name='bloghome'),
    path('<str:cmd>/<int:fa>/<int:la>/',views.bloghome, name='bloghome'), #fa ->first article of page, la->last article
    path('article/',views.article, name='article'),
    path('article/<int:pk>/',views.article, name='article'),
    path('postLike/',views.postLike,name='postLike'), #aid->article id
    path('getLikeCount/',views.getLikeCount,name='getLikeCount'),
    path('postComment/',views.postComment,name='postComment'),
    path('getComments/',views.getComments,name='getComments'),
    path('getAccountStats/',views.getAccountStats,name='getAccountStats')
]