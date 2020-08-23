from django.urls import path

from films_finder import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('reset_bd/', views.reset_bd_view, name='reset_bd'),
]