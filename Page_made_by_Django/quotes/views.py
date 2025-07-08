import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm
from .models import Quote
from django.db.models import Sum



def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        # Проверка на валидность + custom clean из модели
        if form.is_valid():
            form.save()
            return redirect("add_quote")
    else:
        form = QuoteForm()

    return render(request, "add_quote.html", {"form": form})


def random_quote(request):
    total_weight = Quote.objects.aggregate(total=Sum('weight'))['total']
    if total_weight is None or total_weight == 0:
        quote = None
    else:
        target = random.uniform(0, total_weight)
        cumulative_weight = 0
        quote = None

        # Используем order_by('?') + фильтрацию по весу для имитации случайного выбора
        for q in Quote.objects.order_by('id'):
            cumulative_weight += q.weight
            if cumulative_weight >= target:
                quote = q
                break

    return render(request, "quotes/random_quote.html", {"quote": quote})


def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.weight += 1
    quote.save()
    return redirect("quote_detail", quote_id=quote.id)


def dislike_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if quote.weight > 0:
        quote.weight -= 1
        quote.save()
    return redirect("quote_detail", quote_id=quote.id)

def quote_detail(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    return render(request, "quotes/quote_detail.html", {"quote": quote})

def top_quotes(request):
    top_10 = Quote.objects.order_by("-likes")[:10]
    return render(request, "top_quotes.html", {"quotes": top_10})
