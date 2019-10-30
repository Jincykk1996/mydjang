from django.urls import path
from . import views
urlpatterns = [
    path('',views.form),
    path('login/',views.result),
]
