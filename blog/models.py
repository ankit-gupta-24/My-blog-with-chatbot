from django.db import models
# from accounts.models import RegisterUser
from django.conf import settings
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    # likes = models.IntegerField(default=0)
    
    def short_desc(self):
        return self.description[:200]+'....'
    
    def __str__(self):
        return self.title

# model to store article likes
class ArticleLikes(models.Model):
    article_id = models.ForeignKey(Article,on_delete=models.CASCADE )
    liked_by_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# model to store article comments
class ArticleComment(models.Model):
    article_id = models.ForeignKey(Article,on_delete=models.CASCADE )
    commented_by_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_description = models.TextField(max_length=300)

    def __str__(self):
        return  "Article:->"+str(self.article_id.title) + " ||  Comment:->  "+self.comment_description


