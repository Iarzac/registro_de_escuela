import streamlit as st
import sqlite3

def reporte_profesor():
    st.header("Reporte por Profesor")
    profesor = st.text_input("Nombre del Profesor:")
    periodo = st.date_input("Periodo Hasta:")

    if st.button("Generar Reporte"):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT nombre, COUNT(*) FROM materias WHERE profesor = ? GROUP BY nombre",
            (profesor,)
        )
        clases = cursor.fetchall()
        conexion.close()

        if clases:
            st.table(clases)
        else:
            st.warning("No se encontraron registros para ese profesor.")

def reporte_materia():
    st.header("Reporte por Materia")
    materia = st.text_input("Nombre de la Materia:")

    if st.button("Generar Reporte"):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT profesor, COUNT(*) FROM materias WHERE nombre = ? GROUP BY profesor",
            (materia,)
        )
        profesores = cursor.fetchall()
        conexion.close()

        if profesores:
            st.table(profesores)
        else:
            st.warning("No hay registros de esa materia.")

def estadisticas_globales():
    st.header("Estadísticas Globales por Carrera")

    if st.button("Generar Estadísticas"):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT nombre, AVG(creditos) FROM materias GROUP BY nombre"
        )
        estadisticas = cursor.fetchall()
        conexion.close()

        if estadisticas:
            st.table(estadisticas)
        else:
            st.warning("No hay estadísticas disponibles.")
