from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
]
