class Cliente:
    def __init__(self, nombre, apellidos, correo, contrasena, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.contrasena = contrasena
        self.dni = dni
        self.edad = edad

    def registrar(self):
        print("Cliente registrado exitosamente:")
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Correo:", self.correo)
        print("Contrasena:", self.contrasena)
        print("DNI:", self.dni)
        print("Edad:", self.edad)

# Ejemplo de uso
cliente = Cliente("Juan", "Pérez García", "juan@example.com", "contraseña123", "12345678X", 30)
cliente.registrar()
