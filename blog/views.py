from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

def home(request):
    context = {}
    return render(request, 'index.html', context)


def itblog(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    context['carousel_list'] = Carousel.objects.all()
    context['category_list'] = Category.objects.all()
    context['host_article_list'] = Article.objects.order_by('-view_times')[0:10]
    '''paginator = Paginator(article_list,PAGE_NUM)
    page = int(request.GET.get('page'))
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context['articles'] = articles
    '''
    return render(request, 'itblog.html', context)


@ensure_csrf_cookie
def article(request, id = None):
    context = {}
    blog = Article.objects.filter(status=0).get(pk=id)
    comment_list = blog.comment_set.all()
    blog.view_times += 1
    blog.save()
    context['id'] = id
    context['article'] = blog
    context['comment_list'] = comment_list
    return render(request, 'itblog/article.html', context)


def category(request, name=None):
    context = {}
    article_list = Category.objects.get(name=name).article_set.all()
    context['article_list'] = article_list
    context['category_name'] = name
    context['category_list'] = Category.objects.all()
    context['host_article_list'] = Article.objects.order_by('-view_times')[0:10]
    return render(request, 'itblog/category.html', context)


def comment(request, id=None):

    if request.method == 'POST':
        user = request.user
        comment = request.POST.get("comment", "")
        if not user.is_authenticated():
            return HttpResponse('请先登陆！', status=403)
        if not comment:
            return HttpResponse("请输入评论内容", status=403)

        try:
            article = Article.objects.get(id = id)
        except Article.DoesNotExist:
            raise PermissionError

        comment = Comment(
            user=user,
            article=article,
            content=comment,
        )
        comment.save()
        html = "<div>\
                        <a><h4>"+comment.user.username+"</h4></a>"\
                        +"<p>评论："+comment.content+"</p>"+\
                        "<p>"+comment.create_time.strftime("%Y-%m-%d %H:%I:%S")+"</p>\
                    </div><div class='div_hr'></div>"
        return HttpResponse(html)
