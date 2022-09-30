from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    # path('detail/', views.detail),
    # path('new/', views.new),
    # path('edit/', views.edit),
] 