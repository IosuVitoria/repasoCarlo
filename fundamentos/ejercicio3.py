# 3. Cuenta vocales
#    👉 Pista: set de vocales

def cuentavocales (string) :
    vocales = 0
    for character in string:
        if character in "aeiouAEIOUáéíúóé":
            vocales += 1
    
    return vocales

print (cuentavocales("Esto es una prueba de funcionamiento."))

