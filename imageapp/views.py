from django.shortcuts import render
from .forms import ImageForm
# Create your views here.


def home(request):
    form = ImageForm()
    return render(request,'index.html',{'form':form})