from . import views
from django.urls import path

app_name='web'

urlpatterns=[
    path("",views.index,name="index"),
    path("blog/",views.blog,name="blog"),
    path('products',views.products,name='products'),
    path('about', views.about, name="about"),
    path('contact',views.contact, name='contact'),
    path('cart',views.cart, name='cart'),
    path('checkout',views.checkout, name="checkout"),
    path('login',views.login,name='login')
    
]