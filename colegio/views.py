from django.shortcuts import render, redirect
from colegio.models import Usuario, Historial, Alumno, Apoderado, Apoderado, Profesor
from datetime import datetime

def mostrarIndex(request):
    
    return render(request,'index.html')

def mostrarInisesion(request):
    return render(request,'inisesion.html')

def Inisesiona(request):
    if request.method == 'POST':
        nom = request.POST["txtusu"]
        pas = request.POST["txtpas"]

        comprobarLogin = Usuario.objects.filter(nombre_usuario=nom,password_usuario=pas).values()

        if comprobarLogin:
            request.session['estadoSesion'] = True
            request.session['idUsuario'] = comprobarLogin[0]['id']
            request.session['nomUsuario'] = nom.upper()

            datos = {'nomUsuario':nom.upper()}

            descripcion = "Inicia Sesión"
            tabla = ""
            fechayhora = datetime.now()
            usuario = request.session["idUsuario"]
            his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
            his.save()

            if nom.upper() == 'ADMIN':
                return render(request,'menuAdmin.html', datos)
            else:
                return render(request,'menuProfe.html',datos)
        else:
            datos = {'r2': 'error de usuario'}  
            return render(request, 'inisesion.html', datos)
    
    else:
        datos = {'r2': 'Errorerror404'}  # Corregido a un diccionario
        return render(request, 'inisesion.html', datos)
    

def cerrarSesion(request):
    try:
        del request.session['estadoSesion']
        del request.session['nomUsuario']

        descripcion = "Cierra Sesión"
        tabla = ""
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
        his.save()

        del request.session['idUsuario']

        
        return render(request,'inisesion.html')
    except:
        return render(request,'inisesion.html')


def mostrarMenuadmin(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() == "ADMIN":
            datos = { 'nomUsuario' : nomUsuario }
            return render(request, 'menuAdmin.html', datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'inisesion.html', datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'inisesion.html', datos)

#_______________________________________________________

def mostrarFormatricula(request):
    return render(request, "form_matricula.html")

#---------------------------------------------------------------------------


def agregar_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        password_usuario = request.POST['password_usuario']

        descripcion = "agregar usuario"
        tabla = "Usuario"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
        his.save()

        # Verifica si el usuario ya existe
        if not Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            usuario = Usuario(nombre_usuario=nombre_usuario, password_usuario=password_usuario)
            usuario.save()

            # Añade un mensaje de éxito
            datos = {
                'nomUsuario': request.session["nomUsuario"],
                'r': 'Usuario Registrado'
            }

            return render(request, 'agregarUsuario.html', datos)

        mensaje_error = 'El nombre de usuario ya existe. Por favor, elige otro.'
        return render(request, 'agregarUsuario.html', {'mensaje_error': mensaje_error})

    return render(request, 'agregarUsuario.html')
#______________________________________________________________________________________________




#--------------------------------------------------------------------------------------------------------


def mostrarMatriculalumno(request):

    if request.method == "POST":
        rut = request.POST["rut"]
        primer_nombre = request.POST["primer_nombre"]
        segundo_nombre = request.POST.get("segundo_nombre", "")
        apellido_paterno = request.POST["apellido_paterno"]
        apellido_materno = request.POST["apellido_materno"]
        edad = request.POST["edad"]
        nacionalidad = request.POST["nacionalidad"]
        curso = request.POST["curso"]
        sala = request.POST["sala"]

        alumno = Alumno(
            rut=rut,
            primer_nombre=primer_nombre,
            segundo_nombre=segundo_nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            edad=edad,
            nacionalidad=nacionalidad,
            curso=curso,
            sala=sala
        )
        alumno.save()

        descripcion = f"Se registró un nuevo alumno: {primer_nombre} {apellido_paterno}"
        tabla = "Alumno"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(
            descripcion_historial=descripcion,
            tabla_afectada_historial=tabla,
            fecha_hora_historial=fechayhora,
            usuario_id=usuario
        )
        his.save()
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'r': 'Alumno Registrado'
        }
        return render(request, 'form_matricula.html', datos)

    else:
        return render(request, 'menuAdmin.html')
    
    
#_____________________________________________________________________________

def cargarDatosalu(request,id):
    try:
        encontrado = Alumno.objects.get(id=id)

        alum = Alumno.objects.all().values().order_by("id")

        datos = {
            "encontrado" : encontrado,
            "alum" : alum
        }
        return render(request, "listar_usuarios.html",datos)
    
    except:
        alum = Alumno.objects.all().values().order_by("id")

        datos = {
            "encontrado" : encontrado,
            "alum" : alum,
            "r2" : " error el id no existe"
        }
        return render(request, "listar_usuarios.html",datos)



def actualizarAlumno(request, id):
    try:
        rut = request.POST["rut"]
        primer_nombre = request.POST["primer_nombre"]
        segundo_nombre = request.POST["segundo_nombre"]
        apellido_paterno = request.POST["apellido_paterno"]
        apellido_materno = request.POST["apellido_materno"]
        edad = request.POST["edad"]
        nacionalidad = request.POST["nacionalidad"]
        curso = request.POST["curso"]
        sala = request.POST["sala"]

        alumno = Alumno.objects.get(id=id)
        alumno.rut = rut
        alumno.primer_nombre = primer_nombre
        alumno.segundo_nombre = segundo_nombre
        alumno.apellido_paterno = apellido_paterno
        alumno.apellido_materno = apellido_materno
        alumno.edad = edad
        alumno.nacionalidad = nacionalidad
        alumno.curso = curso
        alumno.sala = sala
        alumno.save()

        descripcion = f"Actualización realizada ({primer_nombre} {apellido_paterno})"
        tabla = "Alumno"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        hist = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla,
                         fecha_hora_historial=fechayhora, usuario_id=usuario)
        hist.save()

        profesor = Profesor.objects.all().order_by("id")
        alumnos = Alumno.objects.all().order_by("id")


        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'alumnos' : alumnos,
            'r': 'Datos Modificados Correctamente!!'
        }

        return render(request, 'listar_usuarios.html', datos)

    except Alumno.DoesNotExist:
        profesor = Profesor.objects.all().order_by("id")
        alumnos = Alumno.objects.all().order_by("id")


        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'alumnos' : alumnos,
            'r2': f'El ID ({id}) No Existe. Imposible Actualizar!!'
        }


        return render(request, 'listar_usuarios.html', datos)
    

    

#_________________________________________________________________________________________________

def eliminarAlumno(request, id):
    try:
        alumno = Alumno.objects.get(id=id)
        primer_nombre = alumno.primer_nombre  # Almacena el nombre antes de eliminar
        alumno.delete()

        descripcion = f"Eliminación realizada para el Alumno {primer_nombre}"
        tabla = "Alumno"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        hist = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla,
                         fecha_hora_historial=fechayhora, usuario_id=usuario)
        hist.save()

        alumno = Alumno.objects.all().order_by("id")  

        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'alumno': alumno,
            'r': 'El ID fue eliminado'
        }
        return render(request, 'listar_usuarios.html', datos)

    except Alumno.DoesNotExist:
        alumno = Alumno.objects.all().order_by("id")  

        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'alumno': alumno,
            'r2': 'El ID no existe'
        }
        return render(request, 'listar_usuarios.html', datos)






#--------------------------------------------------------------------------------------------------------



def mostrarMatriculapoderado(request):
    if request.method == "POST":
        rut = request.POST["apoderado_rut"]
        primer_nombre = request.POST["apoderado_primer_nombre"]
        segundo_nombre = request.POST["apoderado_segundo_nombre"]
        apellido_paterno = request.POST["apoderado_apellido_paterno"]
        apellido_materno = request.POST["apoderado_apellido_materno"]
        edad = request.POST["apoderado_edad"]
        parentesco = request.POST["apoderado_parentesco"]
        nacionalidad = request.POST["apoderado_nacionalidad"]

        apoderado = Apoderado(
            rut=rut,
            primer_nombre=primer_nombre,
            segundo_nombre=segundo_nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            edad=edad,
            parentesco=parentesco,
            nacionalidad=nacionalidad
        )
        apoderado.save()

        descripcion = f"Se registró un nuevo apoderado: {primer_nombre} {apellido_paterno}"
        tabla = "Apoderado"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(
            descripcion_historial=descripcion,
            tabla_afectada_historial=tabla,
            fecha_hora_historial=fechayhora,
            usuario_id=usuario
        )
        his.save()
        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'r2': 'Apoderado Registrado'
        }

        return render(request, 'form_matricula.html', datos)  
    else:
        return render(request, 'menuAdmin.html')






#--------------------------------------------------------------------------------------------------------

def mostrarFormprofesores(request):
    return render(request,"profesores.html")

def mostrarGescurso(request):
    return render(request,'gestion_cursos.html')

def mostrarGesalumnos(request):
    return render(request,'gestion_alumnos.html')

#--------------------------------------------------------------------------------------------------------

def registrarProfesores(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        cargo = request.POST["cargo"]
        asignatura = request.POST["asignatura"]

        if Profesor.objects.filter(correo=correo).exists():
            return render(request, 'profesores.html', {'r2': 'Correo ya registrado'})

        profesor = Profesor(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            cargo=cargo,
            asignatura=asignatura
        )
        profesor.save()

        descripcion = f"Se registró un nuevo profesor: {nombre} {apellido}"
        tabla = "Profesor"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(
            descripcion_historial=descripcion,
            tabla_afectada_historial=tabla,
            fecha_hora_historial=fechayhora,
            usuario_id=usuario
        )
        his.save()

        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'r2': 'Profesor Registrado'
        }

        return render(request, 'profesores.html', datos)   

    return render(request, 'menuAdmin.html') 

#________________________________________________________

def mostrarListarprofe(request):
        profesor = Profesor.objects.all().values()
        alumnos = Alumno.objects.all().values()
        usuarios = Usuario.objects.all().values()
        return render(request, "listar_usuarios.html",{'profesor':profesor,'alumnos':alumnos,'usuarios':usuarios})


def cargardatos(request,id):
    try:
        encontrado = Profesor.objects.get(id=id)

        profe = Profesor.objects.all().values().order_by("id")

        datos = {
            "encontrado" : encontrado,
            "profe" : profe
        }
        return render(request, "listar_usuarios.html",datos)
    
    except:
        profe = Profesor.objects.all().values().order_by("id")

        datos = {
            "encontrado" : encontrado,
            "profe" : profe,
            "r2" : " error el id no existe"
        }
        return render(request, "listar_usuarios.html",datos)
    
        




def actualizarProfesor(request,id):
    try:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        cargo = request.POST["cargo"]
        asignatura = request.POST["asignatura"]

        profesor = Profesor.objects.get(id=id)
        profesor.nombre = nombre
        profesor.apellido = apellido
        profesor.correo = correo
        profesor.cargo = cargo
        profesor.asignatura = asignatura
        profesor.save()

        descripcion = f"Actualización realizada ({nombre} {apellido})"
        tabla = "Profesor"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        hist = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla,
                              fecha_hora_historial=fechayhora, usuario_id=usuario)
        hist.save()

        profesor = Profesor.objects.all().order_by("id")
        alumnos = Alumno.objects.all().order_by("id")


        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'alumnos' : alumnos,
            'r': 'Datos Modificados Correctamente!!'
        }

        return render(request, 'listar_usuarios.html', datos)

    except Profesor.DoesNotExist:
        profesor= Profesor.objects.all().order_by("id")
        alumnos = Alumno.objects.all().order_by("id")


        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'alumnos' : alumnos,

            'r2': f'El ID ({id}) No Existe. Imposible Actualizar!!'
        }

        return render(request, 'menuAdmin.html', datos)
    


def eliminarProfesor(request, id):
    try:
        profesor = Profesor.objects.get(id=id)
        nombre_profesor = profesor.nombre  # Almacena el nombre antes de eliminar
        profesor.delete()

        descripcion = f"Eliminación realizada para el profesor {nombre_profesor}"
        tabla = "Profesor"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        hist = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla,
                         fecha_hora_historial=fechayhora, usuario_id=usuario)
        hist.save()

        profesor = Profesor.objects.all().order_by("id")  

        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'r': 'El ID fue eliminado'
        }
        return render(request, 'listar_usuarios.html', datos)

    except Profesor.DoesNotExist:
        profesor = Profesor.objects.all().order_by("id")  

        datos = {
            'nomUsuario': request.session["nomUsuario"],
            'profesor': profesor,
            'r2': 'El ID no existe'
        }
        return render(request, 'listar_usuarios.html', datos)











#-----------------------------------------------------------

def mostrarListarHistorial(request):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            if request.session["nomUsuario"].upper() == "ADMIN":
                his = Historial.objects.select_related("usuario").all().order_by("-fecha_hora_historial")
                datos = {
                    'nomUsuario' : request.session["nomUsuario"],
                    'his' : his
                }
                return render(request, 'listar_historial.html', datos)

            else:
                datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
                return render(request, 'inisesion.html', datos)

        else:
            datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
            return render(request, 'inisesion.html', datos)

    except:
        datos = { 'r2' : 'Error Al Obtener Historial!!' }
        return render(request, 'inisesion.html', datos)

#-----------------------------------------------------------

def mostrarMenuprofe(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() != "ADMIN":
            datos = { 'nomUsuario' : nomUsuario }
            return render(request, 'menuProfe.html', datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'inisesion.html', datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'inisesion.html', datos)
#________________________________________________________________

def mostrarPerfil(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() != "ADMIN":
            datos = { 'nomUsuario' : nomUsuario }
            return render(request, 'perfilProfe.html', datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'inisesion.html', datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'inisesion.html', datos)


    
            