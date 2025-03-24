import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, redirect, url_for, flash, session
from funcionalidad.citas import *
from funcionalidad.emergencias import *
from funcionalidad.historial import *
from funcionalidad.camas import *
from funcionalidad.tda.tda_lista import *
from funcionalidad.auxiliar import *

inicio_archivos()

app = Flask(__name__)
app.secret_key = "clave_secreta_para_flash"  # Necesario para usar flash


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/confirmacion")
def confirmacion():
    return render_template("confirmacion.html")


@app.route("/falla")
def falla():
    return render_template("falla.html")


# --------------------------------------- CITAS ---------------------------------------------------------------
@app.route("/gestion_citas")
def gestion_citas():
    return render_template("gestion_citas/gestion_citas.html")

# --------------------------------------- AGREGAR CITA ---------------------------------------------------------------

@app.route("/agregar_cita")
def agregar_cita():
    return render_template("gestion_citas/agregar_cita.html")

@app.route("/submit_cita", methods=["POST"])
def submit_cita():
    if request.method == "POST":
        # Cargar las citas desde el archivo
        citas = cargar_datos("citas")
        datos = request.form

        # Crear una nueva cita a partir de los datos del formulario
        nueva_cita = cargar_cita(datos, citas)
        citas.insertar(nueva_cita)

        # Guardar las citas actualizadas
        guardar_datos("citas", citas)

        # Obtener el ID de la nueva cita
        id_cita = nueva_cita.mostrar(0)

        # Mensaje flash con el ID de la cita
        flash(f"¡Cita agregada correctamente! ID de la cita: {id_cita}", "success")

        return redirect(url_for("confirmacion"))

# --------------------------------------- MODIFICAR CITA ---------------------------------------------------------------

@app.route("/buscar_modificar")
def buscar_modificar():
    return render_template("gestion_citas/buscar_modificar.html")

@app.route("/modificar_cita", methods=["POST"])
def modificar_cita():
    if request.method == "POST":
        # Cargar las citas desde el archivo
        citas = cargar_datos("citas")
        citas.barrido_adelante()
        # Obtener el ID de la cita desde el formulario
        id_cita =int(request.form.get("id_cita"))
        posicion = obtener_posicion(id_cita)
        if posicion != None:
            # Obtener la cita desde la lista de la TAD
            cita = citas.mostrar(posicion)  # `cita` debería ser una lista (un registro en tu TAD)
        else: 
            flash("Id inexistente, intente nuevamente", "error")
            return redirect(url_for("falla"))
        
        # Crear el diccionario con los datos de la cita
        data = {
            "id": id_cita,  # Ajustar nuevamente a base 1 si es necesario
            "nombre_paciente": cita.mostrar(1),  # Ajusta índices según estructura
            "nombre_medico": cita.mostrar(2),
            "fecha_cita": cita.mostrar(3),
            "estado": cita.mostrar(4),
        }

        # Pasar los datos como parámetros en la redirección
        return render_template("gestion_citas/modificar_cita.html", cita=data)


@app.route("/confirmar_mod_cita", methods=["GET", "POST"])
def confirmar_mod_cita():
    if request.method == "POST":
        # Obtener los datos enviados desde el formulario
        id_cita = request.form.get("id")
        id_cita = int(id_cita)  # Convertir a entero
        nombre_paciente = request.form.get("nombre_paciente")
        nombre_medico = request.form.get("nombre_medico")
        fecha_cita = request.form.get("fecha_cita")
        estado = request.form.get("estado")

        # Validar datos
        if (
            not id_cita
            or not nombre_paciente
            or not nombre_medico
            or not fecha_cita
            or not estado
        ):
            flash("Todos los campos son obligatorios.", "error")
            return redirect(url_for("modificar_cita", id=id_cita))

        # Convertir el ID a índice
        a_modificar = obtener_posicion(id_cita)

        # Cargar las citas desde el archivo
        citas = cargar_datos("citas")

        # Obtener la cita actual
        cita = citas.mostrar(a_modificar)
        estado_anterior = cita.mostrar(4)  # Suponiendo que el estado está en la posición 4

        # Actualizar los datos de la cita
        cita.modificar_nodo(1, nombre_paciente)  # Ajusta índices según estructura
        cita.modificar_nodo(2, nombre_medico)
        cita.modificar_nodo(3, fecha_cita)
        cita.modificar_nodo(4, estado)

        # Agregar al historial solo si:
        # - El estado ha cambiado a "Atendida".
        # - El estado anterior no era "Atendida".
        if estado == "Atendida" and estado_anterior != "Atendida":
            cita_historial(cita)

        # Guardar los cambios
        guardar_datos("citas", citas)

        flash("Cita actualizada con éxito.", "success")
        return redirect(url_for("confirmacion"))

# --------------------------------------- ELIMINAR CITA ---------------------------------------------------------------


@app.route("/buscar_eliminar")
def buscar_eliminar():
    return render_template("gestion_citas/buscar_eliminar.html")


@app.route("/eliminar_cita", methods=["POST"])
def eliminar_cita():
    citas = cargar_datos("citas")
    # Obtener el ID de la cita desde el formulario
    id_cita = request.form.get("id_cita")
    id_cita = int(id_cita) 

    # Obtener el índice (o posición) de la cita a eliminar
    a_eliminar = obtener_posicion(id_cita)      
    print(a_eliminar, "a eliminar")
    
    if a_eliminar != None:
        a_eliminar = int(a_eliminar)
        datos = citas.mostrar(a_eliminar)
        data = {
                "nombre_paciente": datos.mostrar(1),
                "nombre_medico": datos.mostrar(2),
                "fecha": datos.mostrar(3),
                "estado": datos.mostrar(4),
            }
        
        # Renderizar la confirmación con la posición `a_eliminar`
        return render_template("gestion_citas/eliminar_cita.html", a_eliminar=a_eliminar, id_cita = id_cita, data = data)
    else:
        flash("Id inexistente, intente nuevamente", "error")
        return redirect(url_for("falla"))


@app.route("/confirmar_eliminar", methods=["POST"])
def confirmar_eliminar():
    # Cargar las citas desde el archivo
    citas = cargar_datos("citas")
    # Obtener el índice `a_eliminar` desde el formulario
    a_eliminar = int(request.form.get("a_eliminar"))
    id_cita = request.form.get("id_cita")

    # Eliminar la cita utilizando `a_eliminar`
    citas.eliminar_por_posicion(a_eliminar)
    # Guardar los cambios
    guardar_datos("citas", citas)

    # Confirmación de eliminación
    flash(f"Cita ID {id_cita} eliminada con éxito.", "success")
    return redirect(url_for("confirmacion"))

# ----------------------------------- EMERGENCIAS ----------------------------------------------------------
@app.route("/emergencias")
def emergencias():
    return render_template("emergencias/emergencias.html")
# -----------------------------------  CARGA EMERGENCIAS ----------------------------------------------------------

@app.route("/agregar_emergencia")
def agregar_emergencia():
    return render_template("emergencias/agregar_emergencia.html")
@app.route("/submit_emergencia", methods=["POST"])
def submit_emergencia():
    if request.method == "POST":
        # Cargar las citas desde el archivo
        emergencias = cargar_datos("emergencias")
        datos = request.form
        
        # Crear una nueva cita a partir de los datos del formulario
        nueva_emergencia = cargar_emergencia(datos, emergencias)
        emergencias.arribo(nueva_emergencia)

        # Guardar las citas actualizadas
        guardar_datos("emergencias", emergencias)

        # Mensaje flash con el ID de la cita
        flash(f"¡Emergencia agregada correctamente!", "success")

        return redirect(url_for("confirmacion"))

# ----------------------------------- ATENDER EMERGENCIA ----------------------------------------------------------
@app.route("/atender_emergencia")
def atender_emergencia():
    emergencias = cargar_datos("emergencias")
    siguiente = emergencias.atencion()
    guardar_datos('emergencias', emergencias)  
    # Incluir el valor de `siguiente` en el mensaje
    if siguiente:
        historial_emergencia(siguiente)
        flash(f"Siguiente paciente para emergencias: {siguiente}", "success")
        return redirect(url_for('confirmacion'))
    else:
        flash("No hay pacientes en espera para emergencias.", "warning")
        return redirect(url_for('falla'))
    
   

# ----------------------------------- HISTORIAL ----------------------------------------------------------
@app.route("/historial")
def historial():
    return render_template("historial/historial.html")
@app.route("/ver_historial")
def ver_historial():
    historial = mostrar_historial()
    # Procesar la lista para generar descripciones más amigables
    historial_procesado = []
    if historial:  # Verifica si la lista no está vacía
        for item in historial:
            if len(item) == 1:  # Paciente atendido por emergencia
                historial_procesado.append(f"Paciente: <strong>{item[0]}</strong>, atendido por emergencia" )
            elif len(item) == 5:  # Paciente atendido por cita
                historial_procesado.append(
                    f"Paciente: <strong>{item[1]}</strong>, atendido en cita por el Dr/a. <strong>{item[2]}</strong>, el día <strong>{item[3]}</strong>"
                )
    else:
        historial_procesado.append("No se han atendido pacientes.")  # Mensaje si no hay pacientes

    return render_template("historial/ver_historial.html", historial=historial_procesado)

@app.route("/deshacer_ultima")
def deshacer_ultima():
    bandera = deshacer()
    if bandera == True:
        flash(f"Se deshizo la ultima acción", "success")
        return redirect(url_for('confirmacion'))
    else:
        flash(f"No se han atendido pacientes", "success")
        return redirect(url_for('falla'))
# ----------------------------------- ASIGNACION DE CAMAS ----------------------------------------------------------
@app.route("/gestion_camas")
def gestion_camas():
    return render_template("asignacion_camas/gestion_camas.html")

@app.route("/asignar_cama")
def asignar_cama():
    return render_template("asignacion_camas/asignar_cama.html")
# Ruta para procesar los datos del formulario

@app.route("/confirmar_cama", methods=["POST"])
def confirmar_cama():
    if request.method == "POST":
        # Cargar las camas desde el archivo
        raiz = cargar_datos("asignacion_camas")
        data = request.form
        prioridad = data.getlist('prioridad')[0]
        prioridad = int(prioridad)
        raiz, cama = asignar_cama_por_prioridad(raiz, prioridad )
        print(cama)
        inorden(raiz), print("modificado")
        guardar_datos('asignacion_camas', raiz)
        # Mensaje flash con el ID de la cita
        if cama != None:
            flash(f"Cama asignada Nº:{cama}", "success")
            return redirect(url_for("confirmacion"))
        else:
            flash(f"No hay camas disponibles", "success")
            return redirect(url_for('falla'))

@app.route("/liberar_cama")
def liberar_cama():
    return render_template("asignacion_camas/liberar_cama.html")
# Ruta para procesar los datos del formulario

@app.route("/modificar_cama", methods=["POST"])
def modificar_cama():
    if request.method == "POST":
        # Cargar las camas desde el archivo
        raiz = cargar_datos("asignacion_camas")
        data = request.form
        cama = data.getlist('cama')[0]
        cama = int(cama)
        print(cama)
        inorden(raiz)
        nueva = cambiar_disponibilidad(raiz, cama)
        print("Arbol modificado: ")
        inorden(nueva)
        
        if nueva != None:
            guardar_datos('asignacion_camas', nueva)
            flash(f"Cama Nº:{cama} actualizada a disponible.", "success")
            return redirect(url_for("confirmacion"))
        else:
            flash(f"Cama Nº:{cama} ya se encontraba disponible. ", "success")
            return redirect(url_for('falla'))

if __name__ == "__main__":
    app.run(debug=True)