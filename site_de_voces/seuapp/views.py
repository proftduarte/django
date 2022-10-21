from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from seuapp.forms import UsersForm
from seuapp.models import Usuario

# Create your views here.


def cafe(request):
    data = {}
    data['form'] = UsersForm()
    return render(request, 'cafe.html',data)

def dologin(request):
    if request.method == "POST":
        tabela = Usuario.objects.all()
        form = UsersForm(request.POST or None)
        try:
            u = Usuario.objects.get(usuario=request.POST['usuario'])
        except:
            return HttpResponse("Falha no Login")
        print(u)
        if u.senha == request.POST['senha']:
            request.session['uid'] = u.id
            return redirect('home')
        else:
            return HttpResponse("Falha no Login")
    else:
        redirect('cafe')


def home(request):
    profile = {}
    profile['uid'] = request.session['uid']
    return render(request,'home.html',profile)

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html', data)

def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    erro = ''
    for c in tabela:
        if form['usuario'].data == c.usuario :    
            erro ="Mensagem de erro"
    if form.is_valid() and erro == '': 
        form.save()
    return redirect('cafe')