
# 21. Cuenta frecuencia caracteres

def cuenta_frecuencia_caracteres(texto):
    frecuencia = {}

    for caracter in texto:
        if caracter not in frecuencia:
            frecuencia[caracter] = 1
        else:
            frecuencia[caracter] += 1
    
    return frecuencia

texto_test = "lorem impsum, blalbalblablal sfdaada"
print(cuenta_frecuencia_caracteres(texto_test))

# 22. Fusiona diccionarios

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

def unir_diccionarios (dict1, dict2):
    return dict1 | dict2

print(unir_diccionarios(ventas_tienda_1, ventas_tienda_2))

# 23. Invierte clave-valor

def invertir_diccionario(d):
    resultado = {}
    
    for k, v in d.items():
        if v not in resultado:
            resultado[v] = [k]
        else:
            resultado[v].append(k)
    
    return resultado

print(invertir_diccionario(ventas_tienda_2))

# 24. Encuentra valor máximo

ventas_tienda_2 = {
    "naranjas": 25,
    "platanos": 40,
    "peras": 35
}

def encuentra_valor_maximo(diccionarios):
    return max(diccionarios.values())

print(encuentra_valor_maximo(ventas_tienda_2))

# 25. Agrupa palabras por longitud

def agrupar_por_longitud(palabras):
    resultado = {}
    
    for palabra in palabras:
        longitud = len(palabra)
        
        if longitud not in resultado:
            resultado[longitud] = []
        
        resultado[longitud].append(palabra)
    
    return resultado

print(agrupar_por_longitud(["Hola", "esto", "es", "una", "prueba"]))