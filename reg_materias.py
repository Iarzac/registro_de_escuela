import streamlit as st
import sqlite3
import pandas as pd

def mostrar_registro_materia():
    st.header("Registro de Asistencia por Materia")

    """Conectar a la base de datos"""
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    
    """Obtener las materias disponibles"""
    cursor.execute("SELECT id, nombre FROM materias")
    materias = cursor.fetchall()
    conexion.close()

    """Crear un menú desplegable para seleccionar la materia"""
    materia_seleccionada = st.selectbox("Selecciona una materia:", [materia[1] for materia in materias])

    if materia_seleccionada:
        """Conectar de nuevo para obtener los registros de asistencia"""
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT a.profesor, m.nombre, a.fecha 
            FROM asistencia a 
            JOIN materias m ON a.id_materia = m.id 
            WHERE m.nombre = ?""", (materia_seleccionada,))
        registros = cursor.fetchall()
        conexion.close()

        """Mostrar los resultados en una tabla"""
        if registros:
            df = pd.DataFrame(registros, columns=["Profesor", "Materia", "Fecha"])
            st.table(df)
        else:
            st.warning("No hay registros de asistencia para esta materia.")
