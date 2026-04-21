# 26. Suma valores por clave común
# Dado una lista de diccionarios, suma los valores de las claves repetidas.

ventas_tienda_1 = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20
}

ventas_tienda_2 = {
    "naranjas": 25,
    "platanos": 40,
    "peras": 35
}
ventas_tienda_3 = {
    "naranjas": 25,
    "platanos": 40,
    "peras": 35,
    "melones": None,
    "ciruelas": 0
}

def sumar_valores_por_clave (diccionario1, diccionario2):

    for elemento in diccionario1:
        if elemento in diccionario2:
            diccionario1[elemento] = diccionario1[elemento] + diccionario2[elemento]

    for elemento in diccionario2:
        if elemento not in diccionario1:
            diccionario1[elemento] = diccionario2[elemento]

    return diccionario1


print(sumar_valores_por_clave(ventas_tienda_1, ventas_tienda_2))

# 27. Filtra diccionario por valor
# Devuelve solo las claves cuyo valor sea mayor que un umbral dado.

def filtrar_valores_dict (dic, umbral = 0):
    nuevo_diccionario = {}

    for clave, valor in dic.items():
        if valor > umbral:
            nuevo_diccionario[clave] = valor
    
    return nuevo_diccionario

print(filtrar_valores_dict(ventas_tienda_2, 30))

# 28. Ordena diccionario por valor
# Devuelve un diccionario ordenado por sus valores de menor a mayor.

def ordenar_diccionarios(dic):
   return  sorted(dic.items(), key= lambda x : x[1])

print(ordenar_diccionarios(ventas_tienda_2))

# 29. Encuentra clave con mínimo valor
# Devuelve la clave asociada al valor más pequeño del diccionario.

def encuentra_minimo(dic):
    return min(dic.items())

print(encuentra_minimo(ventas_tienda_2))

# 30. Elimina claves con valor nulo
# Elimina todas las claves cuyo valor sea None, 0 o vacío.

def eliminar_clave(dic):
    diccionario_filtrado = {}

    for clave, valor in dic.items():
        if valor != None and valor != 0 and valor != "":
            diccionario_filtrado[clave] = valor

    return diccionario_filtrado

print(eliminar_clave(ventas_tienda_3))
