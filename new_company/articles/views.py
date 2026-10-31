from django.shortcuts import render
from django.http import Http404
from .models import Shipment

def archive(request):
    return render(request, 'archive.html', {"posts": Shipment.objects.all()})

def get_article(request, article_id):
    try:
        # Ищем перевозку по её ID
        post = Shipment.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Shipment.DoesNotExist:
        # Если записи с таким ID нет — стандартная ошибка 404
        raise Http404