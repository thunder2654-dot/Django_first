from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),

    # 회원가입(커스텀)
    path("accounts/", include("accounts.urls")),

    # 로그인/로그아웃(장고 기본)
    path("accounts/", include("django.contrib.auth.urls")),
]