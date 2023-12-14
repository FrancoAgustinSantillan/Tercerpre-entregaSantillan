from datetime import date

from django.shortcuts import redirect, render

# from .models import Cliente, Pais
from . import models
from django import forms
from .models import Cliente
from .forms import ClienteBuscarFormulario


def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)



#def busqueda(request):

    # búsqueda por nombre que contenga "dana"
    cliente_nombre = models.Cliente.objects.filter(nombre__contains="franco")

    # nacimientos mayores a 2000
    cliente_nacimiento = models.Cliente.objects.filter(nacimiento__gt=date(2000, 1, 1))

    # país de origen vacío (null - None)
    cliente_pais = models.Cliente.objects.filter(pais_origen=None)

    context = {
        "cliente_nombre": cliente_nombre,
        "cliente_nacimiento": cliente_nacimiento,
        "cliente_pais": cliente_pais,
    }
    return render(request, "cliente/busqueda.html", context)


from . import forms


def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})



def busqueda(request):
    if request.method == "GET":
        form = ClienteBuscarFormulario()
        return render(
            request,
            "cliente/busqueda.html",
            context={"form": form}
        )
    else:
        formulario = ClienteBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for curso in Cliente.objects.filter(cliente=informacion["nombre"]):
                cursos_filtrados.append(Cliente)

            contexto = {"cliente": cursos_filtrados}
            return render(request, "cliente/busqueda.html", contexto)
