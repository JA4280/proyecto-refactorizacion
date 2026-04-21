# Módulo inicial de procesamiento de ventas
def procesar_registros(registros):
    """
    Procesa una lista de registros de ventas y devoluciones.

    Esta función recorre los registros recibidos y:
    - Valida si es una venta o devolución
    - Aplica descuentos según reglas de negocio
    - Genera un resumen formateado del resultado

    Parámetros:
    registros (list): Lista de diccionarios con información de ventas y devoluciones.   
    """
    # Lista donde se almacenan los resultados finales
    res = []
    for registro in registros:
       
        # Imprimir log de auditoría
        print("Procesando registro de: " + registro['nombre'])
        # Comprobar si es una venta válida
        if validarVenta(registro):
            
            monto = registro['monto']
            esVip = registro['cliente_tipo'] == 'VIP'
            # Aplicar descuento si el monto es alto o es cliente VIP
            if monto > 1000 or (esVip and registro['monto'] > 500):
                montoFinal = monto * 0.9
            else:
                montoFinal = monto            
            # Formatear el resultado
            resultado = "Cliente: " + registro['nombre'] + " - Total: " + str(montoFinal)
            res.append(resultado)
            
        elif registro['tipo'] == 'devolucion' and registro['monto'] > 0:
            # Lógica de devoluciones mezclada
            montoFinal = registro['monto'] * -1
            resultado = "Cliente: " + registro['nombre'] + " - Retorno: " + str(montoFinal)
            res.append(resultado)
  
            
    return res

def validarVenta(registro):
    """
    Valida si un registro corresponde a una venta válida.
    Un registro es considerado una venta válida si:- El tipo es 'venta'    - El monto es mayor a 0    - El estado es 'completado'  
   
    """
    return registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado'

# Datos de prueba para verificar que funciona
datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(procesar_registros(datos_sucios))
