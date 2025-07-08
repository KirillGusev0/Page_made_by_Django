from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        # Поля, которые будут в форме
        fields = ["text", "source", "weight"]
        # Отображение полей
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4}),
            "source": forms.TextInput(attrs={"placeholder": "Фильм, книга и т.д."}),
            "weight": forms.NumberInput(attrs={"min": 1}),
        }
