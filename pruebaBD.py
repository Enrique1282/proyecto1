import sqlite3

conexion = sqlite3.connect("pruebaBD.db")

cursor = conexion.cursor()

archivo = open("pruebaBD.db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS VEHICULOS(
        MATRICULA VARCHAR(10) PRIMARY KEY, 
        MODELO VARCHAR(15), 
        PRECIO INTEGER, 
        COLOR VARCHAR (15)
        )
""")

añadirDatos = [
    ("5515-dsk", "Mercedes", 50000, "gris"), 
    ("1234-sdf", "Renault", 60000, "Marron"), 
    ("8515-jdh", "BMW", 458553, "Negro"), 
    ("5425-uir", "Duty", 52545, "Rojo")
]

cursor.executemany("INSERT INTO VEHICULOS VALUES (?,?,?,?)", añadirDatos)

conexion.commit()

conexion.close()