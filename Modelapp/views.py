from django.shortcuts import render
from Modelapp.forms import StudentsForm

def index(request):
    students=StudentsForm
    return render(request,'index.html',{'form':students})
