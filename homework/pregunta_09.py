"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    diccionario = {}
    with open('files/input/data.csv', mode='r', encoding='utf-8') as archivo:
        for linea in archivo:
            campos = linea.strip().split('\t')
            
            if len(campos) >= 5:
                elementos = campos[4].split(',')
                
                for elemento in elementos:
                    clave = elemento.split(':')[0]
                    if clave not in diccionario:
                        diccionario[clave] = 0
                    diccionario[clave] += 1
                    
    diccionario_ordenado = dict(sorted(diccionario.items()))
            
    return diccionario_ordenado
