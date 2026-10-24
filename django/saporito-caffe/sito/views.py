from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    context = {}
    return render(request, 'sito/home.html', context)


def cart(request):
    context = {}
    return render(request, 'sito/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'sito/checkout.html', context)


def about(request):
    context = {}
    return render(request, 'sito/about.html', context)


def contact(request):
    context = {}
    return render(request, 'sito/contact.html', context)


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sito/store.html', context)


def login(request):
    context = {}
    return render(request, 'sito/login.html', context)
