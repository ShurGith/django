from django.shortcuts import render
from .models import AutorDb
#from django.http import HttpResponse

# Create your views here.

def IndexView(request):
    objeto = AutorDb.objects.all().order_by('-id')
    return render(request, 'index.html',{'objeto':objeto})