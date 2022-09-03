from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request,'index.html')

def prueba(request):
    var = "holaaaaaaaaaa"
    return HttpResponse(f"<p>el mensaje es este: {var}</p>")