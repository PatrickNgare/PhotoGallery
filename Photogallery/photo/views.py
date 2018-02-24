from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery,Location,Category
# Create your views here.

def index(request):
    

    photos=Gallery.objects.all()

    return render(request,'index.html',{"photos": photos })