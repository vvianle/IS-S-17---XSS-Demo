from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import UserLoginForm, UserRegisterForm

# @csrf_exempt
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    print (request.POST)
    print (request)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        response = redirect("/")
        response.set_cookie("username", user.username)
        return response
    return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        response = redirect("/")
        response.set_cookie("username", user.username)
        return response

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")