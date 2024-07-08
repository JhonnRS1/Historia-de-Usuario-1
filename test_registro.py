from registro import Cliente

def test_registro_cliente_exitoso():
    cliente = Cliente("Juan", "Pérez García", "juan@example.com", "contrasena123", "12345678X", 30)
    resultado = cliente.registrar()
    assert True == resultado
