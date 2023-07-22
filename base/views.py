from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    content=Content.objects.all()
    print(content)
    context = {'contents':content}
    return render(request, 'base/index.html',  context)

def About(request):
    context = {}
    return render(request, 'base/about.html',  context)


def Contact(request):
    context = {}
    return render(request, 'base/contact.html',  context)

def Exercise(request):
    context = {}
    return render(request, 'base/exercises.html',  context)

def Mcq(request):
    context = {}
    return render(request, 'base/mcqs.html',  context)

def Quiz(request):
    context = {}
    return render(request, 'base/quizes.html',  context)
