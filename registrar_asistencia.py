import streamlit as st
import sqlite3

def registrar_asistencia():
    """Registra la asistencia de un profesor a una clase específica."""
    st.header("Registrar Asistencia")

    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    conexion.close()

    """Seleccionar materia y profesor, y elegir la fecha"""
    materia_seleccionada = st.selectbox("Selecciona una materia:", [materia[1] for materia in materias])
    profesor = st.text_input("Nombre del Profesor:")
    fecha = st.date_input("Fecha de la Clase:")

    if st.button("Registrar Asistencia"):
        """Validar que la materia y el profesor coincidan en la base de datos"""
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM materias WHERE nombre = ? AND profesor = ?",
            (materia_seleccionada, profesor)
        )
        resultado = cursor.fetchone()

        if resultado:
            """Insertar el registro de asistencia"""
            cursor.execute(
                "INSERT INTO asistencia (id_materia, profesor, fecha) VALUES (?, ?, ?)",
                (resultado[0], profesor, str(fecha))
            )
            conexion.commit()
            st.success("Asistencia registrada exitosamente.")
        else:
            st.error("La materia o el profesor no están registrados.")

        conexion.close()
