from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('<int:month>', views.monthly_challenge_by_number, name='MonthNumber'),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),

]
