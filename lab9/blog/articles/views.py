from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from .models import Article
from django.contrib.auth import authenticate, login

def create_post(request):

    if not request.user.is_authenticated:
        raise Http404()

    if request.method == "POST":

        form = {
            "title": request.POST.get("title"),
            "text": request.POST.get("text")
        }

        # проверка заполнения
        if not form["title"] or not form["text"]:
            form["errors"] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})

        # проверка уникальности
        if Article.objects.filter(title=form["title"]).exists():
            form["errors"] = "Статья с таким названием уже существует"
            return render(request, "create_post.html", {"form": form})

        # создаем статью
        article = Article.objects.create(
            title=form["title"],
            text=form["text"],
            author=request.user
        )

        return redirect("get_article", article_id=article.id)

    return render(request, "create_post.html", {})


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

def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        art = None
        try:
            art = User.objects.get(username=form["username"])
            art = User.objects.get(email=form["mail"])
            # если номер существует, то ошибки не произойдет и
            # программа удачно доберется до следующей строчки
            print(u"Такой номер уже есть")
        except User.DoesNotExist:
            print(u"Такого номера ещё нет")
        if form["username"] and form["mail"] and form["password"] and art is None:
            art = User.objects.create_user(username=form["username"],
                                           email=form["mail"],
                                           password=form["password"])
            return redirect(archive)
        else:
            if art is not None:
                form['errors'] = u"Логин или почта уже заняты"
            else:
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})

def input_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(request, username=form["username"], password=form["password"])
            if user is None:
                form['errors'] = u'Такой пользователь не зарегистрирован!'
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, user)
                return redirect(archive)
        else:
            form['errors'] = u'Не все поля заполнены'
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html', {})
