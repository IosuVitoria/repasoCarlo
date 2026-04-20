# 2. Comprueba si es palíndromo
#    👉 Pista: compara con reverso

def palindromo (string):
    return string[::-1] == string;

print(palindromo("Wolaaa"));
print(palindromo("ala"));