from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('login/', views.login, name="login"),
]
