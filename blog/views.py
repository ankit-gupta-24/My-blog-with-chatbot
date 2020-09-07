from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Article, ArticleLikes,ArticleComment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def bloghome(request,cmd=None,fa=None,la=None):
    articles = Article.objects.all()
    articles = sorted(articles,key = lambda x:x.pub_date,reverse=True)
    if request.method=='POST':
        searchkey = request.POST.get('searchblog').lower()
        searchedArtl = []
        ct = 0

        for artl in articles:
            if searchkey in artl.title.lower() or searchkey in artl.tags.lower():
                searchedArtl.append(artl)
                ct+=1
            if ct>50:
                break

        context = {
            'articles':searchedArtl,
            'btn_display':False,
        }
        return render(request,'blog/index.html',context)
    else:   
       
        if cmd=='prev':
            if fa <= 0 or fa-5 <=0:
                fa=0
                la=4
            elif fa-5>=0:
                fa = fa -5
                la = la -5
        elif cmd == 'next':
            if (la >= len(articles)-1) or (la + 5 > len(articles)):
                fa = len(articles)-5
                la = len(articles)-1
            else:
                fa = la+1
                la = la+5
        else:
            fa = 0
            la = 4
        
        articles = articles[fa:la+1]

        context = {
            'articles':articles,
            'first_article': articles[0].id-1,
            'last_article': articles[len(articles)-1].id-1,
            'btn_display':True,
        }

    return render(request,'blog/index.html',context)



def article(request,pk=None):
    if pk == None:
        return bloghome(request)

    article = Article.objects.get(id=pk)

    context= {
        'article':article,
        'comment_form': CommentForm()
    }
    return render(request,'blog/display_single_article.html',context)


@login_required(login_url='/accounts/loginForm')
def postLike(request):
    if request.method == 'POST':
        if request.is_ajax():
            username = request.POST['username']
            userObj = User.objects.get(username=username)

            aid = int(request.POST['aid'])
            aIdObj = Article.objects.get(id=aid)

            if len(ArticleLikes.objects.filter(article_id=aIdObj, liked_by_username=userObj)) < 1:
                obj = ArticleLikes(article_id=aIdObj,liked_by_username=userObj)
                obj.save()                   
            total_likes = len(ArticleLikes.objects.filter(article_id=aIdObj))
            return HttpResponse(total_likes)


@login_required(login_url='/accounts/loginForm')
def getLikeCount(request):
    if request.method == 'POST':
        if request.is_ajax():
            aid = int(request.POST['aid'])
            aIdObj = Article.objects.get(id=aid)
            total_likes = len(ArticleLikes.objects.filter(article_id=aIdObj))

            return HttpResponse(total_likes)   


@login_required(login_url='/accounts/loginForm')
def postComment(request):
    if request.method == 'POST':     
        if request.is_ajax():
            cmnt_desc = request.POST['cmnt_desc']
            artl = int(request.POST['artl_id'])
            username = request.POST['username']
            
            artl_obj = Article.objects.get(id=artl)
            user_obj = User.objects.get(username=username)

            frm = ArticleComment(article_id = artl_obj, commented_by_username=user_obj, comment_description=cmnt_desc)
            frm.save()
            
    return HttpResponse('success')


@login_required(login_url='/accounts/loginForm')
def getComments(request):
    if request.method == 'POST':
        if request.is_ajax():
            artl = int(request.POST['artl_id'])
            artl_obj = Article.objects.get(id=artl)

            data = ArticleComment.objects.filter(article_id=artl_obj).values('article_id__id','commented_by_username__username','comment_description')
            # print(data)
            data = json.dumps(list(reversed(data)), cls=DjangoJSONEncoder)

    return JsonResponse({'all_artl_comments':data})


@login_required(login_url='/accounts/loginForm')
def getAccountStats(request):
    if request.method == 'POST':
        total_article_count = len(Article.objects.all())
        total_comment_count = len(ArticleComment.objects.filter(commented_by_username__username=request.user.username))
        total_like_count = len( ArticleLikes.objects.filter(liked_by_username__username= request.user.username) )

        context = {
            'total_article_count':total_article_count,
            'total_comment_count':total_comment_count,
            'total_like_count':total_like_count,
        }

        return JsonResponse(context)
    return render(request,'accounts/loginForm.html')
