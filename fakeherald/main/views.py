from django.shortcuts import render
from .models import Author, Comment, Article

# Create your views here.
def index(request):
	article_list = Article.objects.all()
	return render(request,'index.html', {'article_list' : article_list})

def article(request, article_id):
	article = Article.objects.get(pk=article_id)
	return render(request,'article.html', {'article' : article})
