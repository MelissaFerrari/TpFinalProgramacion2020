import csv

def leer_archivo(path, columna):
    arreglo = []
    with open(path) as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        lector.__next__() #salteamos primer fila (titulo de la columna)
        for fila in lector:
            dato = fila[0] #me quedo con el primer elemento (por algun motivo es un arreglo de un solo elemento con todo adentro)
            dato2 = dato.split(",") # rompo el elemento donde haya una coma
            valor = dato2[columna] # me quedo con el 3°
            arreglo.append(float(valor)) # Lo mando al resultado
        return arreglo
