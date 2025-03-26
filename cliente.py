class Cliente:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.telefono = None
        self.rfc = None
        self.email = None

    # Getters
    def getId(self): return self.id
    def getNombre(self): return self.nombre
    def getTelefono(self): return self.telefono
    def getRfc(self): return self.rfc
    def getEmail(self): return self.email

    # Setters
    def setId(self, id): self.id = id
    def setNombre(self, nombre): self.nombre = nombre
    def setTelefono(self, telefono): self.telefono = telefono
    def setRfc(self, rfc): self.rfc = rfc
    def setEmail(self, email): self.email = email