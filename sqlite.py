import sqlite3

def crear_base_datos():
    """Crea la base de datos y las tablas necesarias si no existen."""
    conexion = sqlite3.connect('escuela.db')
    cursor = conexion.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        profesor TEXT NOT NULL,
        creditos INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asistencia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_materia INTEGER,
        profesor TEXT,
        fecha TEXT,
        FOREIGN KEY (id_materia) REFERENCES materias (id)
    )
    ''')

    conexion.commit()
    conexion.close()

crear_base_datos()
