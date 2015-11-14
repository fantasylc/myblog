from django.shortcuts import render
from .models import *
from .forms import MessageForm
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from markdown import markdown
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.core.mail import send_mail

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


def suibiall(request):
    context = {}
    article_list = Suibi.objects.all()
    context['article_list'] = article_list
    return render(request, 'suibiall.html',context)


@ensure_csrf_cookie
def article(request, id = None):
    context = {}
    blog = Article.objects.filter(status=0).get(pk=id)
    comment_list = blog.comment_set.all()
    blog.view_times += 1
    blog.save()
    blog.content = markdown(blog.content,['codehilite'])
    context['id'] = id
    context['article'] = blog
    context['comment_list'] = comment_list
    return render(request, 'itblog/article.html', context)


@ensure_csrf_cookie
def suibi(request, id = None):
    context = {}
    blog = Suibi.objects.filter(status=0).get(pk=id)
    comment_list = blog.commentsuibi_set.all()
    blog.view_times += 1
    blog.save()
    blog.content = markdown(blog.content,['codehilite'])
    context['id'] = id
    context['article'] = blog
    context['comment_list'] = comment_list
    return render(request, 'itblog/suibi.html', context)


def about(request):
    context = {}
    return render(request,'about.html',context)


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


def commentsuibi(request, id=None):
    if request.method == 'POST':
        user = request.user
        comment = request.POST.get("comment", "")
        if not user.is_authenticated():
            return HttpResponse('请先登陆！', status=403)
        if not comment:
            return HttpResponse("请输入评论内容", status=403)

        try:
            suibi = Suibi.objects.get(id = id)
        except Suibi.DoesNotExist:
            raise PermissionError

        commentsuibi = Commentsuibi(
            user=user,
            article=suibi,
            content=comment,
        )
        commentsuibi.save()
        print('hello')
        html = "<div>\
                        <a><h4>"+commentsuibi.user.username+"</h4></a>"\
                        +"<p>评论："+commentsuibi.content+"</p>"+\
                        "<p>"+commentsuibi.create_time.strftime("%Y-%m-%d %H:%I:%S")+"</p>\
                    </div><div class='div_hr'></div>"
        return HttpResponse(html)


def leavemessage(request):
    context = {}
    if request.GET.get('newsn')=='1':
        csn=CaptchaStore.generate_key()
        cimageurl= captcha_image_url(csn)
        return HttpResponse(cimageurl)


    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            message = request.POST.get('message')

            if not name and not message:
                return HttpResponse('请输入内容',status=403)

            leave_message = Leavemessage(
            name = name,
            message = message
            )
            leave_message.save()
            '''
            title = '欢迎来到superliu.me'
            message = "%s留言:\n"%(name)+"内容是:\n%s"(message)
            from_email = ''
            send_mail(title,message,from_email,[email])
            '''
            form = MessageForm()
            context['form'] = form
            context['yesorno'] = '感谢你的留言，已收到～'
            return render(request,'message.html',context)
        else:
            context['form'] = form
            return render(request,'message.html',context)
    if request.method == 'GET':
        form = MessageForm()
        context['form'] = form
        return render(request,'message.html',context)