from django.shortcuts import render, get_object_or_404
from .models import  Article
from comments.forms import  CommentsForm
# Create your views here.

def index(request):

    article_list = Article.objects.all().order_by('-created_time')
    a1_list = article_list[:2]
    a2_list = article_list[2:5]
    a3_list = article_list[5:]
    context = {
        "article_list":article_list,
        "a1_list":a1_list,
        "a2_list":a2_list,
        "a3_list":a3_list,
        }
    return render(request, 'myblog/index.html',context = context)

def detail(request, pk):
    article = get_object_or_404(Article, pk = pk)
    form = CommentsForm()
    comment_list = article.comments_set.all()
    context = {'article': article,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, "myblog/detail.html", context )

