from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.index, name='index'),
    path('create/', views.create, name='create'),
]
