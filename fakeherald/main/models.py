from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE,default=2)

class Visitor(models.Model):
	name = models.CharField(max_length=20)
	user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)

class Article(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles', default=None)

class Comment(models.Model):
	text = models.TextField()
	pub_date = models.DateTimeField()
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='comments', blank=True, default=None, null=True)
 


# models.IntegerField()