from django.contrib import admin
from django.urls import path
from colegio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mostrarIndex),
    path('mostrar_login',views.mostrarInisesion, name='login'),
    path('login',views.Inisesiona),
    path('logout',views.cerrarSesion),


    path('menuAdmin',views.mostrarMenuadmin, name='menuadmin'),
    path('agregar_usuario',views.agregar_usuario),
    path('form_matricula',views.mostrarFormatricula),
    path('matriculaAlumno',views.mostrarMatriculalumno),
    path('matriculaApoderado',views.mostrarMatriculapoderado),
    
    path('profesores',views.mostrarFormprofesores),
    path('registrar_profesor',views.registrarProfesores),
    
    path('listar_usuarios',views.mostrarListarprofe ),
    path('actualizar_profe/<int:id>', views.actualizarProfesor, name='actualizar_profe'),
    path('actualizar_alumno/<int:id>', views.actualizarAlumno,),

    path('cargar_datos/<int:id>',views.cargardatos),
    path('cargar_datosa/<int:id>',views.cargarDatosalu),

    path('eliminar_profesor/<int:id>', views.eliminarProfesor , name='eliminar_profe'),
    path('eliminar_alumno/<int:id>', views.eliminarAlumno , name='eliminar_alumno'),


    path('listar_historial', views.mostrarListarHistorial),


    path('menuProfe',views.mostrarMenuprofe, name='menuprofe'),
    path('perfil_profe',views.mostrarPerfil, name='perfil_profe'),
    path('gestion_curso',views.mostrarGescurso),
    path('gestion_alumnos',views.mostrarGesalumnos)


]
