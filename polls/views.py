# polls/views.py
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Question, Choice
from .forms import QuestionForm


# ===== Read (List) =====
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        qs = Question.objects.all()

        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(question_text__icontains=q)

        sort = self.request.GET.get("sort", "new")
        if sort == "old":
            qs = qs.order_by("pub_date")
        else:
            qs = qs.order_by("-pub_date")

        return qs


# ===== Read (Detail) =====
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"


# ===== Read (Results) =====
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"


# ===== Create =====
class QuestionCreateView(generic.CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")


# ===== Update =====
class QuestionUpdateView(generic.UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "polls/question_form.html"
    success_url = reverse_lazy("polls:index")


# ===== Delete =====
class QuestionDeleteView(generic.DeleteView):
    model = Question
    template_name = "polls/question_confirm_delete.html"
    success_url = reverse_lazy("polls:index")


# ===== Vote =====
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # 동시성 안전하게 +1
        Choice.objects.filter(pk=selected_choice.pk).update(votes=F("votes") + 1)
        return HttpResponseRedirect(reverse_lazy("polls:results", kwargs={"pk": question.id}))
