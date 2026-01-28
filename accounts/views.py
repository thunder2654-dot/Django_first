from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 가입 직후 로그인
            return redirect("polls:index")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})