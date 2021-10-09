import numpy as np

def obtener_numero_mes(mes): # no se usa pero queda por si se usa mas adelante, es para unificar formatos de columna
    MESES = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]
    return MESES.index(mes) + 1

def igualar_arreglos(x, y):
    tamano_x = len(x)
    tamano_y = len(y)
    if (tamano_x == tamano_y):
        return [x, y]
    else:
        diferencia = abs(tamano_x - tamano_y) # abs() retorna el valor absoluto (por si da negativo)
        if (tamano_x > tamano_y):
            nuevo_arreglo = np.array(x)
            recortado = nuevo_arreglo[0:len(nuevo_arreglo)-diferencia]
            return [recortado, np.array(y)]
        else:
            nuevo_arreglo = np.array(y)
            recortado = nuevo_arreglo[0:len(nuevo_arreglo)-diferencia]
            return [np.array(x), recortado]

def calcular_correlacion(x, y):
    return np.corrcoef(x, y)

def imprimir_correlacion(c):
    print('*************************************')
    print()
    if (c > 0):
        print('Existe correlacion entre los datos!! :D', c)
    else:
        print('No existe correlacion :(', c)
    print()
    print('*************************************')