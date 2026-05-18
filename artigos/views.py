from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def is_author(user):
    return user.is_authenticated and user.groups.filter(name="autores").exists()


def articles_view(request):
    articles = Article.objects.all().order_by("-created_at")

    return render(request, "artigos/articles.html", {
        "articles": articles
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    comments = article.comments.all().order_by("-created_at")

    form = CommentForm(request.POST or None)

    if request.method == "POST" and request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()

            return redirect("article_detail", pk=pk)

    return render(request, "artigos/article_detail.html", {
        "article": article,
        "comments": comments,
        "form": form
    })


@login_required
@user_passes_test(is_author)
def article_create(request):
    form = ArticleForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        return redirect("articles")

    return render(request, "artigos/form.html", {
        "form": form,
        "title": "Criar Artigo"
    })


@login_required
@user_passes_test(is_author)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)

    form = ArticleForm(
        request.POST or None,
        request.FILES or None,
        instance=article
    )

    if form.is_valid():
        form.save()
        return redirect("articles")

    return render(request, "artigos/form.html", {
        "form": form,
        "title": "Editar Artigo"
    })


@login_required
def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return redirect("article_detail", pk=pk)