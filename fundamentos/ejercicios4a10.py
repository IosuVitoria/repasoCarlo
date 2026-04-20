# 4. Elimina duplicados manteniendo orden
#    👉 Pista: usa set + lista

def eliminar_duplicados (lista):
    return list(set(lista))

lista_test = [1,2,3,4,5,5,5,5,6,6,6,6,6,7,8,9]
print (lista_test)
print (eliminar_duplicados(lista_test))

# 5. Encuentra el carácter más frecuente
#    👉 Pista: diccionario

def encuentraCaracterMasFrecuente (string):
    cuentaCaracteres = {}

    for character in string:
        if character not in cuentaCaracteres:
            cuentaCaracteres[character] = 1
        else:
            cuentaCaracteres[character] += 1
    
    caracter_mas_frecuente = max(cuentaCaracteres, key=cuentaCaracteres.get)

    return caracter_mas_frecuente;

print(encuentraCaracterMasFrecuente("Este es un texto de prueba"))

# 6. Capitaliza primera letra de cada palabra
#    👉 Pista: split + join

def capitalizaPalabras(string):
    palabras = string.split()
    palabras_capitalizadas = [p.capitalize() for p in palabras]
    return " ".join(palabras_capitalizadas)

print(capitalizaPalabras("este es un texto de prueba"))

# 7. Reemplaza espacios por guiones
#    👉 Pista: replace

def reemplazaEspacios(string):
    return string.replace(" ", "-")

print(reemplazaEspacios("Este es un texto de prueba."))

# 8. Cuenta palabras
#    👉 Pista: split()

def contarPalabras(string):
    return len(string.split(" "))

print(contarPalabras("Esto es como se cuentan palabras."))

# 9. Encuentra primera letra no repetida
#    👉 Pista: frecuencia

def primeraNoRepetida(string):
    frecuencia = {}

    for char in string:
        frecuencia[char] = frecuencia.get(char, 0) + 1

    for char in string:
        if frecuencia[char] == 1:
            return char

    return None

print(primeraNoRepetida("aabbcddex"))

# 10. Comprueba si dos strings son anagramas
#     👉 Pista: sorted()

def sonAnagramas(str1, str2):
    return sorted(str1) == sorted(str2)

print(sonAnagramas("roma", "amor"))