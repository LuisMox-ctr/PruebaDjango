from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def contacto(request):
    return render(request,"registros/contactos.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            print("Datos:", form.cleaned_data)
            form.save()
            return redirect('ver_comentarios')
        else:
            print("Formulario inválido:", form.errors)
    else:
        form = ComentarioContactoForm()
    return render(request, 'registros/contactos.html', {'form': form})

def ver_comentarios(request):
        Comentarios = ComentarioContacto.objects.all()
        return render(request,'registros/ver_comentarios.html',{'comentarios':Comentarios})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('ver_comentarios')
    else:
        form = ComentarioContactoForm(instance=comentario)

    return render(request, 'registros/formEditarComentario.html', {'form': form, 'comentario': comentario})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        # Redirige a la vista que muestra la lista de comentarios
        return redirect('ver_comentarios')
    return render(request, confirmacion, {'object': comentario})

def consulta1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta2(request):
    alumnos=Alumnos.objects.filter(carrera="Ti").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","turno","imagen","carrera")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consulta4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consulta5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta6(request):
    fechaInicio = datetime.date(2025,7,)
    fechaFin= datetime.date(2025,7,30)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta7(request):
    alumnos=Alumnos.objects.filter(comentario__texto__icontains="No inscrito")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultaSQL(request):
    alumnos=Alumnos.objects.raw('select id, matricula,nombre,carrera,turno, imagen from registros_alumnos where carrera="TI" order by turno desc')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def seguridad(request, nombre=None):
    nombre= request.GET.get('nombre')
    return render(request,"registros/seguridad.html",
    {'nombre':nombre})

#//////////////////////////////////////////////////////////////////////////////////////////////////////
def consulta8(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 15)
    comentarioContacto = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request,"registros/ver_comentarios.html",{'comentarios':comentarioContacto})

def consulta9(request):
    comentarioContacto=ComentarioContacto.objects.filter(mensaje__icontains="Santas vacas")
    return render(request,"registros/ver_comentarios.html",{'comentarios': comentarioContacto})
def consulta10(request):
    comentarioContacto=ComentarioContacto.objects.filter(usuario__in=["user1","user2"])
    return render(request,"registros/ver_comentarios.html",{'comentarios':comentarioContacto})

def consulta11(request):
    comentarioContacto=ComentarioContacto.objects.all().only("mensaje")
    return render (request,"Registros/ver_comentarios.html",{'comentarios':comentarioContacto})

def consulta12(request):
    comentarioContacto=ComentarioContacto.objects.order_by("created")
    return render(request,"Registros/ver_comentarios.html", {'comentarios':comentarioContacto})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.FILES['archivo']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, 
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request,"Error al procesar el formulario")
    else:
            return render(request,"registros/archivos.html",{'archivo':Archivos})
