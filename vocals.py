texto = "alkhjklhk lkhlkhlkjalñjñlroñjoij"
# vocal = ["a","e","i","o","u"]
''' for letra in texto:
    if letra in "aeiou":
        if letra not in vocales_texto:
            vocales_texto.append(letra)
print(vocales_texto)'''

vocales_texto = [letra for letra in texto if letra in "aeiou"]
print(type(vocales_texto))
vocales_texto2 = set(vocales_texto)
print(type(vocales_texto2))
result1 = list(vocales_texto2)
print(result1)
