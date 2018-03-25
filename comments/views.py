#redirect函数对http请求重定向

from django.shortcuts import render,get_object_or_404,redirect
from myblog.models import Article
from .models import Comments
from .forms import  CommentsForm
# Create your views here.


def post_comment(request, post_pk):
    post = get_object_or_404(Article, pk = post_pk)

    if request.method == "POST":
        form = CommentsForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()

            return redirect(post)
        else:
            comment_list = post.comments_set.all().order_by("-Created_time")
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list,
                       }
            return render(request, 'myblog/detail.html', context = context)

    return redirect("myblog:detail", pk = post_pk)


