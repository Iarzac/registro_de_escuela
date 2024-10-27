import streamlit as st
import sqlite3
import pandas as pd

def mostrar_registro_profesor():
    st.header("Registro de Clases por Profesor")

    """Conectar a la base de datos"""
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    
    """Obtener los profesores disponibles"""
    cursor.execute("SELECT DISTINCT profesor FROM asistencia")
    profesores = cursor.fetchall()
    conexion.close()

    """Crear un menú desplegable para seleccionar el profesor"""
    profesor_seleccionado = st.selectbox("Selecciona un profesor:", [profesor[0] for profesor in profesores])

    if profesor_seleccionado:
        """Conectar de nuevo para obtener los registros de asistencia"""
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT m.nombre, a.fecha 
            FROM asistencia a 
            JOIN materias m ON a.id_materia = m.id 
            WHERE a.profesor = ?""", (profesor_seleccionado,))
        registros = cursor.fetchall()
        conexion.close()

        """Mostrar los resultados en una tabla"""
        if registros:
            df = pd.DataFrame(registros, columns=["Materia", "Fecha"])
            st.table(df)
        else:
            st.warning("No hay registros de clases impartidas por este profesor.")
