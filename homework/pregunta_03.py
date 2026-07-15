"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    lista = []
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            campos = linea.split('\t')
            if len(campos) > 1:
                lista.append((campos[0], int(campos[1])))
    return [(i, sum(x[1] for x in lista if x[0] == i)) for i in sorted(set(x[0] for x in lista))]
