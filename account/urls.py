from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('', views.pro, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('cont/<int:id>', views.cont, name='cont'),
    path('checkout/', views.checkout, name='checkout'),
    path('coupon/', views.coupon, name='coupon'),
]
