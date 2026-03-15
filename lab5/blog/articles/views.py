from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article

def create_post(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            # обработать данные формы
            form = {
                "text": request.POST.get("text"),
                "title": request.POST.get("title")
            }

            if form["text"] and form["title"]:
                # ПРОВЕРКА УНИКАЛЬНОСТИ
                if Article.objects.filter(title=form["title"]).exists():
                    form["errors"] = "Статья с таким названием уже существует"
                    return render(request, "create_post.html", {"form": form})
                    article = Article.objects.create(
                        text=form["text"],
                        title=form["title"],
                        author=request.user
                    )

                    return redirect("get_article", article_id=article.id)

                else:
                    # если введенные данные некорректны
                    form["errors"] = "Не все поля заполнены"
                    return render(request, "create_post.html", {"form": form})

        else:
            # если метод GET
            return render(request, "create_post.html", {})

    else:
        raise Http404()

def archive(request):
    return render(request, 'archive.html', {
        "posts": Article.objects.all()
    })

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found")

    return render(request, 'article.html', {
        "post": post
    })
