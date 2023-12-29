from django.shortcuts import render, redirect, HttpResponse

from management import models
from management.utils.form import LoginForm, RegisterForm


def login(request):
    form = LoginForm()
    context = {
        "form": form
    }

    if request.method == "GET":
        print("this is get")
        return render(request, 'login.html', context)

    form = LoginForm(data=request.POST)

    print("post")
    # print(request.GET)
    # print(request.POST)

    if form.is_valid():
        user_object = models.User.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            print(form.errors)
            context['form'] = form
            return render(request, 'login.html', context)

            # 去数据库校验
        user_object = models.User.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")

            print(form.errors)
            return render(request, 'login.html', {"form": form})

        # 用户名和密码输入正确
        # 网站生成随机字符串，写到用户的浏览器的cookie中，再写入到session中
        request.session["info"] = {'id': user_object.id, 'name': user_object.username}
        # 用户信息可以保存 7 天
        request.session.set_expiry(60 * 60 * 24 * 14)
        return redirect('/student/list/')

    print("not valid")
    context['form'] = form
    return render(request, 'login.html', context)


def logout(request):
    # 注销
    request.session.clear()
    return redirect('/login/')


def register(request):
    form = RegisterForm()
    context = {
        "form": form
    }
    if request.method == "GET":
        return render(request, 'register.html', context)

    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        print("register valid")
        return redirect("/login/")

    context['form'] = form
    print("register valid")
    return render(request, 'register.html', context)
