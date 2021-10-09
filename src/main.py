
import sys

from numpy.lib.function_base import corrcoef
from constants.constants import PATH_PRECIPITACIONES, PATH_VIENTOS
from functions.archivos import leer_archivo
from functions.calculos import calcular_correlacion, igualar_arreglos, imprimir_correlacion

cantidad_archivos = sys.argv[1] # leo el segundo argumento de la linea de comandos, que es la cantidad de archivos

columna = 2

precipitaciones = leer_archivo(PATH_PRECIPITACIONES, columna)
vientos = leer_archivo(PATH_VIENTOS, columna)

recortados = igualar_arreglos(precipitaciones, vientos) #recorto el mas grande del mismo tamaño del mas chico

precipitaciones = recortados[0]
vientos = recortados[1]

matriz_correlacion = calcular_correlacion(precipitaciones, vientos)

correlacion = matriz_correlacion[0][int(cantidad_archivos) - 1] # la ultima columna de la matriz de correlacion es #archivos - 1

imprimir_correlacion(correlacion) #imprimo bonito