from django.shortcuts import render

# Create your views here.

def course(request, chair, course, pk):
    print(request, chair, course, pk)
