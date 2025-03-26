from conexion import Conexion
import cliente as model

class DbCliente:
    def __init__(self):
        self.conexion = Conexion()

    def save(self, cliente):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nombre, telefono, rfc, email) VALUES (%s, %s, %s, %s)"
        values = (cliente.getNombre(), cliente.getTelefono(), cliente.getRfc(), cliente.getEmail())
        cursor.execute(sql, values)
        conn.commit()
        self.conexion.close()

    def search(self, cliente):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "SELECT * FROM clientes WHERE id = %s"
        cursor.execute(sql, (cliente.getId(),))
        row = cursor.fetchone()
        self.conexion.close()
        
        if row:
            cliente = model.Cliente()
            cliente.setId(row[0])
            cliente.setNombre(row[1])
            cliente.setTelefono(row[2])
            cliente.setRfc(row[3])
            cliente.setEmail(row[4])
            return cliente
        return None

    def edit(self, cliente):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "UPDATE clientes SET nombre = %s, telefono = %s, rfc = %s, email = %s WHERE id = %s"
        values = (cliente.getNombre(), cliente.getTelefono(), cliente.getRfc(), cliente.getEmail(), cliente.getId())
        cursor.execute(sql, values)
        conn.commit()
        self.conexion.close()

    def remove(self, cliente):
        conn = self.conexion.open()
        cursor = conn.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (cliente.getId(),))
        conn.commit()
        self.conexion.close()