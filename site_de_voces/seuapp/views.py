from django.shortcuts import render

# Create your views here.
a = 0

def home(request):
	return render(request,'home.html',{'variavel': a })

def cafe(request):
    return render(request, 'cafe.html',{})

def nova_pagina(request):
    return render(request, 'nova_pagina.html',{})