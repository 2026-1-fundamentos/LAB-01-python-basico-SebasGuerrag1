"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    lista = []
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            campos = linea.split('\t')
            if len(campos) > 1:
                lista.append((campos[0], int(campos[1])))
    return [(i, max(x[1] for x in lista if x[0] == i), min(x[1] for x in lista if x[0] == i)) for i in sorted(set(x[0] for x in lista))]
