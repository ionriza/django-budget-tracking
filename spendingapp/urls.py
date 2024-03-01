from django.urls import path
from . import views

urlpatterns = [
    path('', views.spending,name='spending'),
    path('adauga/',views.adauga,name='adauga')

]