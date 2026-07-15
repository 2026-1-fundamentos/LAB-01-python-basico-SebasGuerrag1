"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    diccionario = {}
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        for linea in archivo:
            campos = linea.strip().split('\t')
            if len(campos) >= 5:
                clave = campos[0]
                valores = campos[4].split(',')
                suma_valores = sum(int(valor.split(':')[1]) for valor in valores)
                
                if clave not in diccionario:
                    diccionario[clave] = 0
                diccionario[clave] += suma_valores

    return dict(sorted(diccionario.items()))
