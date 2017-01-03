from django.shortcuts import render

def display(request):
   return  render(request,'html/index.html')
