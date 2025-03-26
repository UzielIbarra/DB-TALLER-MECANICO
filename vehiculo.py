class Vehiculo:
    def __init__(self):
        self.matricula = None
        self.cliente = None
        self.marca = None
        self.modelo = None
        self.color = None

    # Getters
    def getMatricula(self): return self.matricula
    def getCliente(self): return self.cliente
    def getMarca(self): return self.marca
    def getModelo(self): return self.modelo
    def getColor(self): return self.color

    # Setters
    def setMatricula(self, matricula): self.matricula = matricula
    def setCliente(self, cliente): self.cliente = cliente
    def setMarca(self, marca): self.marca = marca
    def setModelo(self, modelo): self.modelo = modelo
    def setColor(self, color): self.color = color