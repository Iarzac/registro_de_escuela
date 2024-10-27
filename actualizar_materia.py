import streamlit as st
import sqlite3

def actualizar_materia():
    """Función para actualizar la información de una materia en la base de datos."""
    st.header("Actualizar Materia")

    nombre = st.text_input("Nombre de la Materia a Actualizar:")
    nuevo_profesor = st.text_input("Nuevo Nombre del Profesor:")

    if st.button("Actualizar"):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE materias SET profesor = ? WHERE nombre = ?",
            (nuevo_profesor, nombre)
        )
        conexion.commit()
        conexion.close()
        st.success("Materia actualizada exitosamente.")

