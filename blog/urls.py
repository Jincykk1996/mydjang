from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.p, name='home'),
    path('blog/', views.p1, name='blog'),
    path('register/', views.p3, name='register'),
    path('login/', views.p4, name='login'),
    path('logout/', views.p5, name='logout'),
    path('blog/<int:id>/', views.p6, name='bpost'),
    path('search/', views.p7, name='search'),
    path('create/', views.p8, name='create'),
    path('update/<int:id>/', views.p9, name='update'),
    path('delete/<int:id>/', views.p10, name='delete'),
    path('comment/', views.p11, name='comment'),
]

