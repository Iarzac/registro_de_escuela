import streamlit as st
import sqlite3
from materias import agregar_materia
from borrar_materia import borrar_materia
from mostrar_datos import mostrar_datos
from leer_registros import leer_registros
from actualizar_materia import actualizar_materia
from generar_pdf import generar_pdf
from reg_materias import mostrar_registro_materia
from reg_profesores import mostrar_registro_profesor
from registrar_asistencia import registrar_asistencia


st.set_page_config(page_title="Sistema de Registro de Clases", layout="centered")

def main():
    """Función principal de la aplicación que maneja la navegación entre opciones."""
    st.title("Sistema de Registro de Clases para Control de Asistencia Docente")

    opcion = st.sidebar.selectbox(
        "Selecciona una opción:",
        ["Agregar Materia", "Borrar Materia", "Leer Registros", 
         "Mostrar Datos", "Actualizar Materia", "Generar PDF", "Registrar Asistencia",
         "Mostrar Registro de Materia", "Mostrar Registro de Profesor"]
    )

    """Llamar la funcionalidad correspondiente"""
    if opcion == "Agregar Materia":
        agregar_materia()
    elif opcion == "Borrar Materia":
        borrar_materia()
    elif opcion == "Leer Registros":
        leer_registros()
    elif opcion == "Mostrar Datos":
        mostrar_datos()
    elif opcion == "Actualizar Materia":
        actualizar_materia()
    elif opcion == "Generar PDF":
        generar_pdf()
    elif opcion == "Registrar Asistencia":
        registrar_asistencia()
    elif opcion == "Mostrar Registro de Materia":
        mostrar_registro_materia()
    elif opcion == "Mostrar Registro de Profesor":
        mostrar_registro_profesor()

if __name__ == "__main__":
    main()
