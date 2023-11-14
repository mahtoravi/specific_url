from django.urls import path
from mi.views import *
app_name='something'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumrah/',bumrah,name='bumrah'),
]