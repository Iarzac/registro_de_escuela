import streamlit as st
import sqlite3
from fpdf import FPDF

def generar_pdf():
    """Genera un reporte en formato PDF con las materias registradas."""
    st.header("Generar Reporte PDF")

    """Conectar a la base de datos y obtener las materias"""
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    conexion.close()

    """Configuración del PDF"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Registro de Materias", ln=True, align="C")
    pdf.ln(10)

    """Crear encabezados de tabla"""
    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 10, "ID", 1)
    pdf.cell(60, 10, "Materia", 1)
    pdf.cell(50, 10, "Profesor", 1)
    pdf.cell(30, 10, "Créditos", 1)
    pdf.ln()

    """Insertar datos en la tabla"""
    pdf.set_font("Arial", size=12)
    for materia in materias:
        pdf.cell(30, 10, str(materia[0]), 1)
        pdf.cell(60, 10, materia[1], 1)
        pdf.cell(50, 10, materia[2], 1)
        pdf.cell(30, 10, str(materia[3]), 1)
        pdf.ln()

    """Guardar el PDF y mostrar botón de descarga"""
    pdf.output("reporte_materias.pdf")
    st.success("PDF generado exitosamente.")
    st.download_button(
        "Descargar PDF", data=open("reporte_materias.pdf", "rb"), file_name="reporte_materias.pdf"
    )
