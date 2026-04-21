# 11. Encuentra máximo
#     👉 Pista: recorre

def encuentraMaximo(lista):
    return (max(lista))

print(encuentraMaximo([1,2,4,5,65,5]))

# 12. Encuentra mínimo

def encuentraMinimo(lista):
        return min(lista)

print(encuentraMinimo([1,2,3,4,55,66,54]))

# 13. Suma elementos

lista_test = [1,2,3,4,5,6,7,8]

def sumaElementos(lista):
      return sum(lista);

print(sumaElementos(lista_test))

# 14. Elimina duplicados
#     👉 Pista: set

lista_test_2 = [1,2,2,2,2,3,3,3]

def eliminarDuplicados(lista):
      return list(set(lista))

print(eliminarDuplicados(lista_test_2))

# 15. Invierte lista
#     👉 Pista: slicing

def invertirLista(lista):
    return lista[::-1]

print(invertirLista(lista_test_2))

# 16. Encuentra segundo mayor
#     👉 Pista: sort o dos pasadas

def encuentra_segundo_mayor(lista):
    lista_ordenada = sorted(list(set(lista)), reverse=True)

    if len(lista_ordenada) < 2:
        return None
    
    return lista_ordenada[1]

print(encuentra_segundo_mayor(lista_test))
print(encuentra_segundo_mayor([5,5,5,5]))

# 17. Cuenta ocurrencias

def cuenta_ocurrencias(lista):
    ocurrencias = {}

    for elemento in lista:
        if elemento not in ocurrencias:
            ocurrencias[elemento] = 1
        else:
            ocurrencias[elemento] += 1
    
    return ocurrencias

print(cuenta_ocurrencias(lista_test_2))
         
# 18. Filtra pares

def filtrar_pares(lista):
    return list(filter(lambda x : x%2 == 0, lista))

print(filtrar_pares(lista_test_2))

# 19. Multiplica todos los elementos

def multiplica_elementos(lista):
    return list(map(lambda x : x* 2, lista ))

print(multiplica_elementos(lista_test_2))

# 20. Encuentra índice de un elemento

def encuentra_indice_elemento(lista, elemento):
    return lista.index(elemento);

print(encuentra_indice_elemento(lista_test_2, 2))