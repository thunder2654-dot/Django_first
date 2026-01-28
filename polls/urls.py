# polls/urls.py
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # Read
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # CRUD (Question)
    path("new/", views.QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/edit/", views.QuestionUpdateView.as_view(), name="question_update"),
    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question_delete"),
]