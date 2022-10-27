from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from seuapp.forms import UsersForm,ComentariosForm
from seuapp.models import Usuario,Comentario

# Create your views here.


def cafe(request):
    data = {}
    data['form'] = UsersForm()
    return render(request, 'cafe.html',data)

def dologin(request):
    if request.method == "POST":
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

def dologout(request):
    if request.session['uid'] != "" or request.session['uid'] != None:
        try:
            del request.session['uid'] # apaga a sessão
            return HttpResponse("Sessão finalizada")
        except KeyError:
            return redirect('home')
    return redirect('home')    


def home(request):
    profile = {}
    try:
        profile['perfil'] = Usuario.objects.get(id=request.session['uid'])
        profile['custom'] = "LOGOUT"
    except KeyError:
        profile['custom'] = "LOGIN"
    print(profile['custom'])
    return render(request,'home.html', profile)

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

def profile(request):
    profile = {}
    try:
        profile['perfil'] = UsersForm(instance=Usuario.objects.get(id=request.session['uid']))
        return render(request,'profile.html', profile)
    except:
        return HttpResponse("vc não está logado")
def do_update(request):
    form= Usuario.objects.get(id=request.session['uid'])
    form.usuario = request.POST['usuario']
    form.nome = request.POST['nome']
    form.ultimo_nome = request.POST['ultimo_nome']
    form.save()
    return redirect('home')



def comentario(request):
    data ={}
    if request.method == 'POST':
        c = Comentario(usuario=Usuario.objects.get(id=request.session['uid']),comentario=request.POST['comentario'])
        c.save()
        return redirect('comentario')
    else:
        data['form'] = ComentariosForm()
        print(data['form'])
        return render(request,'comentario.html',data)

