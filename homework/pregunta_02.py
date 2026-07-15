"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    lista = []
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            campos = linea.split('\t')
            if len(campos) > 0:
                lista.append(campos[0])
    return [(i, lista.count(i)) for i in sorted(set(lista))]
