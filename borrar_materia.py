import streamlit as st
import sqlite3

def reindexar_ids():
    """Reindexa los IDs de las materias para mantener consecutividad."""
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()

    """Seleccionar todas las materias y reinsertarlas con nuevos IDs consecutivos"""
    cursor.execute("SELECT * FROM materias ORDER BY id")
    materias = cursor.fetchall()
    cursor.execute("DELETE FROM materias")
    for index, materia in enumerate(materias, start=1):
        cursor.execute(
            "INSERT INTO materias (id, nombre, profesor, creditos) VALUES (?, ?, ?, ?)",
            (index, materia[1], materia[2], materia[3])
        )

    conexion.commit()
    conexion.close()

def borrar_materia():
    """Función para eliminar una materia de la base de datos."""
    st.header("Borrar Materia")

    """Solicitar el nombre de la materia a eliminar"""
    nombre = st.text_input("Nombre de la Materia a Eliminar:")

    if st.button("Borrar Materia"):
        """Eliminar la materia y reindexar los IDs"""
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM materias WHERE nombre = ?", (nombre,))
        conexion.commit()
        conexion.close()

        st.success(f"Materia '{nombre}' eliminada.")
        reindexar_ids()  
