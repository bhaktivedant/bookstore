
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg),
    path('login', views.log),
    path('user',views.userdetails),
    path('edit/<int:pk>',views.edituser,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('product',views.bookdetails),
    path('book',views.bookview,name='bookview'),
    path('addcart/<int:pk>',views.addtocart,name='addcart'),
    path('cart',views.viewcart),
    path('cartdelete/<int:pk>',views.cartdelete,name='cartdelete'),
  
   
    
]
