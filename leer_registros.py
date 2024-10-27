import streamlit as st
import sqlite3

def leer_registros():
    """Lee y muestra todas las materias registradas en la base de datos."""
    st.header("Leer Registros")

    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    conexion.close()

    for materia in materias:
        st.write(f"ID: {materia[0]}, Nombre: {materia[1]}, Profesor: {materia[2]}, Créditos: {materia[3]}")
