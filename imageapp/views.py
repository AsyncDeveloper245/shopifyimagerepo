from django.shortcuts import render
from .forms import ImageForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        form  = ImageForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            form.save()
    form = ImageForm()
    return render(request,'index.html',{'form':form})

def delete(request,id):
    pass

def update(request,id):
    pass

