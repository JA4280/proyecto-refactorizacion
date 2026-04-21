# Módulo inicial de procesamiento de ventas
def procesar_registros(registros):
    # Esta función hace muchas cosas a la vez
    res = []
    for registro in registros:
        # Comprobar si es una venta válida
        if validarVenta(registro):
            # Aplicar descuento si el monto es alto o es cliente VIP
            if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
                montoFinal = registro['monto'] * 0.9
            else:
                montoFinal = registro['monto']
            
            # Formatear el resultado
            resultado = "Cliente: " + registro['nombre'] + " - Total: " + str(montoFinal)
            res.append(resultado)
            
            # Imprimir log de auditoría (duplicado innecesario)
            print("Procesando registro de: " + registro['nombre'])
        elif registro['tipo'] == 'devolucion' and registro['monto'] > 0:
            # Lógica de devoluciones mezclada
            montoFinal = registro['monto'] * -1
            resultado = "Cliente: " + registro['nombre'] + " - Retorno: " + str(montoFinal)
            res.append(resultado)
            print("Procesando registro de: " + registro['nombre'])
            
    return res

def validarVenta(registro):
    return registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado'

# Datos de prueba para verificar que funciona
datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_registros(datos_sucios))
