# 🏥 Sistema de Gestión de Reservas y Servicios Médicos

Este proyecto es un **sistema de reservas y servicios médicos** para un hospital, desarrollado en **Python**, con una **interfaz web** utilizando **HTML** y **CSS**. Se emplearon diversas **estructuras de datos** para optimizar la gestión de citas, atención de emergencias, historial de pacientes y asignación de camas.

## 📌 Características

### ✅ **1. Gestión de citas médicas**
- Uso de una **lista** para administrar las citas programadas.
- Cada cita incluye **ID, paciente, médico, fecha y estado** (pendiente, atendida, cancelada).
- Funciones implementadas:
  - Agregar una cita.
  - Modificar una cita.
  - Cancelar una cita.

### 🚑 **2. Atención de pacientes de emergencia**
- Uso de una **cola (FIFO)** para gestionar emergencias médicas.
- Los pacientes son atendidos en orden de llegada.
- Funciones implementadas:
  - Agregar un paciente a la cola.
  - Atender a un paciente (eliminarlo de la cola).

### 📜 **3. Historial de pacientes atendidos**
- Uso de una **pila (LIFO)** para registrar pacientes atendidos.
- Al atender un paciente, se transfiere de la lista o cola al historial.
- Funciones implementadas:
  - Ver historial de pacientes.
  - Deshacer la última atención registrada.

### 🏨 **4. Asignación de camas de hospitalización**
- Uso de un **árbol binario de búsqueda** para gestionar camas.
- Cada nodo representa una cama con **número, disponibilidad y prioridad** (gravedad del paciente).
- Funciones implementadas:
  - Asignar una cama según gravedad.
  - Actualizar cama a disponible.

## 🎨 Interfaz gráfica
- Se implementa un **menú interactivo** para gestionar todas las funciones del sistema.
- La interfaz fue desarrollada con **HTML** y **CSS** para proporcionar una experiencia de usuario intuitiva y fácil de usar.

## 📸 Captura de pantalla

![Menú del sistema](https://github.com/exequiel-exe/Gestion_Hospitalaria-Proyecto-/blob/main/images/Captura_de_Menu.png?raw=true)

## 🛠 Tecnologías utilizadas
- **Python** 🐍
- **HTML y CSS** para la interfaz web 🖥️
- **Estructuras de datos (Lista, Cola, Pila, Árbol Binario)** 📂
- **Manejo de archivos para persistencia de datos** 📄

## 📢 Notas importantes
- **Todas las estructuras de datos fueron implementadas manualmente.**
- **El sistema almacena datos en archivos para persistencia.**
- **Debe ejecutarse en un entorno con Python 3.8 o superior.**



