from conexion import Conexion
import vehiculo as model

class DbVehiculo:
    def __init__(self):
        self.conexion = Conexion()

    def save(self, vehiculo):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = """INSERT INTO vehiculos 
                (matricula, cliente_id, marca, modelo, color) 
                VALUES (%s, %s, %s, %s, %s)"""
        values = (vehiculo.getMatricula(), vehiculo.getCliente(), 
                 vehiculo.getMarca(), vehiculo.getModelo(), 
                 vehiculo.getColor())
        cursor.execute(sql, values)
        conn.commit()
        self.conexion.close()

    def search(self, vehiculo):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "SELECT * FROM vehiculos WHERE matricula = %s"
        cursor.execute(sql, (vehiculo.getMatricula(),))
        row = cursor.fetchone()
        self.conexion.close()
        
        if row:
            vehiculo = model.Vehiculo()
            vehiculo.setMatricula(row[0])
            vehiculo.setCliente(row[1])
            vehiculo.setMarca(row[2])
            vehiculo.setModelo(row[3])
            vehiculo.setColor(row[4])
            return vehiculo
        return None

    def edit(self, vehiculo):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = """UPDATE vehiculos 
                SET cliente_id = %s, marca = %s, 
                    modelo = %s, color = %s 
                WHERE matricula = %s"""
        values = (vehiculo.getCliente(), vehiculo.getMarca(),
                 vehiculo.getModelo(), vehiculo.getColor(),
                 vehiculo.getMatricula())
        cursor.execute(sql, values)
        conn.commit()
        self.conexion.close()

    def remove(self, vehiculo):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "DELETE FROM vehiculos WHERE matricula = %s"
        cursor.execute(sql, (vehiculo.getMatricula(),))
        conn.commit()
        self.conexion.close()