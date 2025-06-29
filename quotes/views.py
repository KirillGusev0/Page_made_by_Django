from django.shortcuts import render, redirect
from .forms import QuoteForm

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