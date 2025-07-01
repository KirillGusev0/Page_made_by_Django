
import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm
from .models import Quote
from django.http import HttpResponseRedirect
from django.urls import reverse

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




def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.likes += 1
    quote.save()
    return HttpResponseRedirect(reverse('random_quote'))

def dislike_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.dislikes += 1
    quote.save()
    return HttpResponseRedirect(reverse('random_quote'))

def top_quotes(request):
    top_10 = Quote.objects.order_by('-likes')[:10]
    return render(request, 'top_quotes.html', {'quotes': top_10})