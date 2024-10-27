import streamlit as st
import sqlite3
import pandas as pd

def mostrar_datos():
    """Muestra las materias registradas en forma de tabla."""
    st.header("Mostrar Datos")

    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    conexion.close()

    if materias:
        df = pd.DataFrame(materias, columns=["ID", "Materia", "Profesor", "Créditos"])
        st.table(df)
    else:
        st.warning("No hay materias registradas.")
