from django.urls import path
from . import views
urlpatterns = [
    # path('',views.forl),
    path('<int:id>/', views.prod)
]