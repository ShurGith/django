from django.urls import path
from .views import IndexView,AutorView

urlpatterns =[
    path('', IndexView),
    path('autor/<int:id>',AutorView),
   # path('autor/<int:id>', AutorView, name="AutorName"), # Indicamos que usaremos autor/ y un parametro int
]