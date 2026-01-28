# polls/forms.py
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        widgets = {
            "question_text": forms.TextInput(attrs={"placeholder": "질문을 입력하세요"}),
            "pub_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
