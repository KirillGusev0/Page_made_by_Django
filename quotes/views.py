
import random
from django.shortcuts import render, redirect
from .forms import QuoteForm
from .models import Quote

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)

        # Проверка на валидность + custom clean из модели
        if form.is_valid():
            form.save()
            return redirect('add_quote')  
    else:
        form = QuoteForm()

    return render(request, 'add_quote.html', {'form': form})




def random_quote(request):
    # Получаем все цитаты с их весами
    quotes = list(Quote.objects.all())
    if not quotes:
        return render(request, 'random_quote.html', {'quote': None})

    # Готовим список весов
    weights = [quote.weight for quote in quotes]

    # Выбираем случайную цитату с учётом веса
    selected = random.choices(quotes, weights=weights, k=1)[0]

    # Увеличиваем счётчик просмотров
    selected.views += 1
    selected.save()

    return render(request, 'random_quote.html', {'quote': selected})