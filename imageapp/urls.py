from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [
    path('',views.home,name='home'),
    path('/image/<int:id>',views.home,name='gallery'),

]