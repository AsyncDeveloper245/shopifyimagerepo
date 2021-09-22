from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Image
# Create your views here.


def home(request,id=None):
    if request.method == 'POST':
        form  = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    images = Image.objects.all()
    form = ImageForm()
    return render(request,'index.html',{'form':form,'images':images})

def delete(request,id):
    Image.objects.get(pk=id).delete()
    return redirect('image:home')

def update(request,id):
    pass

