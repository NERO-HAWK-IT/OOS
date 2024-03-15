from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounting/', views.accounting, name='accounting'),
    path('review/', views.review, name='review'),
    path('reports/', views.reports, name='reports'),
]
