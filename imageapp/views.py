from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.


def home(request,id=None):
    if request.method == 'POST':
        form  = ImageForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form = form.cleaned_data
            image = Image.objects.create(
                name = form['name'],
                image = form['image'],
                description = form['description'],
            )
            instance = form.save(commit=False)
            instance.save()
    images = Image.objects.all()
    form = ImageForm()
    return render(request,'index.html',{'form':form,'images':images})

def delete(request,id):
    if request.method == 'POST':
        image = Image.objects.get(pk=id)
        image.delete()

def update(request,id):
    pass

