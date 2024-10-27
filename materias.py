import streamlit as st
import sqlite3

def agregar_materia():
    """Permite agregar una nueva materia a la base de datos."""
    st.header("Agregar Materia")

    """Entrada de datos para la nueva materia"""
    nombre = st.text_input("Nombre de la Materia:")
    profesor = st.text_input("Nombre del Profesor:")
    creditos = st.number_input("Número de Créditos:", min_value=1, step=1)

    if st.button("Agregar Materia"):
        if nombre and profesor:
            conexion = sqlite3.connect('escuela.db')
            cursor = conexion.cursor()

            """Obtener el próximo ID disponible"""
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM materias")
            nuevo_id = cursor.fetchone()[0]

            """Insertar la materia en la base de datos"""
            cursor.execute(
                "INSERT INTO materias (id, nombre, profesor, creditos) VALUES (?, ?, ?, ?)",
                (nuevo_id, nombre, profesor, creditos)
            )
            conexion.commit()
            conexion.close()

            st.success("Materia agregada exitosamente.")
        else:
            st.error("Por favor, completa todos los campos.")
