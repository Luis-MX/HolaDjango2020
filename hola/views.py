from django.shortcuts import render
from .forms import FormArticulo


def def_hola(request):
    context = {
        'nombre':'alex',
        'edad': 39,
        'materias':[
            {'nombre':'Frameworks','cal':10},
            {'nombre': 'Deployment','cal':8},
            {'nombre': 'Testing','cal':9},
            {'nombre': 'Linux','cal':6},
        ]
    }
    return render(request, 'hola.html', context)

def def_login(request):
    
    if request.method == 'POST':
        user = request.POST.get('username', None)
        passwd = request.POST.get('password', None)

        mensaje = 'Datos incorrectos'
        if user == 'alex' and passwd == '123':
            mensaje = 'Datos correctos'
        return render(request, 'login.html',{'mensaje':mensaje})

    return render(request, 'login.html')

def def_articulo(request):
    if request.method == 'POST':
        form = FormArticulo(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request, 'articulo.html', {'form':form})

    form = FormArticulo()
    return render(request, 'articulo.html', {'form':form})
