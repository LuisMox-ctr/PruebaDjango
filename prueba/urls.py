"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros,name="principal"),
    path('contacto/',views_registros.contacto,name="contacto"),
    path('formulario/',views.formulario,name="formulario"),
    path('ejemplo/',views.ejemplo,name="ejemplo"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('comentarios/',views_registros.ver_comentarios,name="ver_comentarios"),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto,name='Editar'),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('consultas1',views_registros.consulta1,name="Consultas"),
    path('consultas2',views_registros.consulta2,name="Consultas2"),
    path('consultas3',views_registros.consulta3,name="Consultas3"),
    path('consultas4',views_registros.consulta4,name="Consultas4"),
    path('consultas5',views_registros.consulta5,name="Consultas5"),
    path('consultas6',views_registros.consulta6, name="Consultas6"),
    path('consultas7',views_registros.consulta7, name="Consultas7"),
    path('consultas8',views_registros.consulta8, name="Consultas8"),
    path('consultas9',views_registros.consulta9, name="Consultas9"),
    path('consultas10',views_registros.consulta10, name="Consultas10"),
    path('consultas11',views_registros.consulta11, name="Consultas11"),
    path('consultas12',views_registros.consulta12, name="Consultas12"),
    path('subir', views_registros.archivos, name="Subir"),
    path('consultaSQL', views_registros.consultaSQL, name="SQL"),
    path('seguridad',views_registros.seguridad,name="Seguridad"),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
    

