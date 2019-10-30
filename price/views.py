from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Price

class PriceListView(ListView):
    model=Category
    template_name='price/index.html'

def PriceDetailView(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        price=Price.objects.filter(category=category.id)
    except Category.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'price/detail.html', {'category': category, 'price':price})