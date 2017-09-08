# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import BlogCategory,BlogPost,UserProfile
from .forms import ArticleForm,SearchForm
# Create your views here.

def get_all(request):
    all_category = BlogCategory.objects.all()
    all_blog = BlogPost.objects.all()

    hot_clickblogs = BlogPost.objects.order_by('-poll_num')[:6]
    hot_newblogs = BlogPost.objects.order_by('-add_time')[:6]
    hot_tuiblogs = hot_clickblogs
    return {"all_category":all_category,
            "all_blog":all_blog,
            "hot_clickblogs":hot_clickblogs,
            "hot_newblogs":hot_newblogs,
            "hot_tuiblogs":hot_tuiblogs}

class IndexView(View):
    def get(self, request):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]
        all_blog = blog_dict["all_blog"]
        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 6, request=request)
        blogs = p.page(page)

        return render(request, "index.html", {"all_category":all_category,
                                              "all_blog":blogs,
                                              "hot_clickblogs":hot_clickblogs,
                                              "hot_newblogs":hot_newblogs,
                                              "hot_tuiblogs":hot_tuiblogs})


class BlogContentView(View):
    def get(self, request, blog_id):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]
        all_blog = blog_dict["all_blog"]
        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        my_blog = BlogPost.objects.get(id=blog_id)
        my_blog.poll_num += 1
        my_blog.save()
        if my_blog:
            return render(request, "blog_view.html", {"my_blog":my_blog,
                                                      "all_category": all_category,

                                                      "hot_clickblogs": hot_clickblogs,
                                                      "hot_newblogs": hot_newblogs,
                                                      "hot_tuiblogs": hot_tuiblogs
                                                      })


class AddArticleView(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, "add_aritcle.html", {"form":form})


class ListArticleView(View):
    def get(self, request, type):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]

        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        blogcate = BlogCategory.objects.get(name=type)
        blogs = blogcate.blogpost_set.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(blogs, 6, request=request)
        blogs = p.page(page)

        return render(request, "blog_type.html", {"all_category":all_category,
                                              "all_blog":blogs,
                                              "hot_clickblogs":hot_clickblogs,
                                              "hot_newblogs":hot_newblogs,
                                              "hot_tuiblogs":hot_tuiblogs,
                                               "blogcate":blogcate })


class SearchView(View):
    """搜索"""
    def post(self, request):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]
        all_blog = blog_dict["all_blog"]
        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        form = SearchForm(request.POST)
        if form.is_valid():
            aticlename = request.POST.get("article_name", "")

            blogs = BlogPost.objects.filter(title__icontains=aticlename)
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            p = Paginator(blogs, 6, request=request)
            blogs = p.page(page)
            return render(request, "index.html", {"all_category": all_category,
                                                  "all_blog": blogs,
                                                  "hot_clickblogs": hot_clickblogs,
                                                  "hot_newblogs": hot_newblogs,
                                                  "hot_tuiblogs": hot_tuiblogs,
                                                  "form":form})
        else:
            return render(request, "index.html", {"all_category": all_category,
                                                  "all_blog": all_blog,
                                                  "hot_clickblogs": hot_clickblogs,
                                                  "hot_newblogs": hot_newblogs,
                                                  "hot_tuiblogs": hot_tuiblogs})

class AboutView(View):
    def get(self, request):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]
        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        userpro = UserProfile.objects.get(name='Sachin')

        return render(request, "about_my.html", {"all_category": all_category,
                                                      "hot_clickblogs": hot_clickblogs,
                                                      "hot_newblogs": hot_newblogs,
                                                      "hot_tuiblogs": hot_tuiblogs,
                                                  "usermsg":userpro})

class LiuyanView(View):
    def get(self,request):
        blog_dict = get_all(request)
        all_category = blog_dict["all_category"]
        hot_clickblogs = blog_dict["hot_clickblogs"]
        hot_newblogs = blog_dict["hot_newblogs"]
        hot_tuiblogs = blog_dict["hot_tuiblogs"]

        return render(request, "liuyanban.html", {"all_category": all_category,
                                              "hot_clickblogs": hot_clickblogs,
                                              "hot_newblogs": hot_newblogs,
                                              "hot_tuiblogs": hot_tuiblogs})


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response