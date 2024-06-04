import random

list_hinds = ["Es una comida italina", "Lleva tomate", "Suele llevar carne", "En italiano se llama 'penne'", "Es una pasta"]
list_hinds2 = ["Es una comida española", "Lleva patatas", "Hay una version 'cutre' en Francia", "Puede llevar cebolla", "Es redonda"]
list_hinds3 = ["Es una comida italiana", "Es redonda", "Lleva queso", "Lleva tomate", "Puede llevar jamon"]
## Primer bucle para que meta un numero de intentos validos
MAX_INTENTOS = len(list_hinds)

dicc_words = {
    1: {"macarrones": list_hinds },
    2: {"tortilla de patatas": list_hinds2},
    3: {"pizza": list_hinds3}
}

random_number = random.randint(0, len(dicc_words))
print(random_number)
print(dicc_words[random_number])
correct_word = dicc_words[random_number].keys()[0]
input_usuario = input("Adivina la comida: ")

## Segundo bucle para que adivine la comida
for i in range(0,MAX_INTENTOS):
    if input_usuario == correct_word:
        print("Has acertado!")
        break
    else:
        print("Has fallado!")
        print("pista:", dicc_words.get(random_number).get(correct_word)[i])
        input_usuario = input("Vuelve a intentarlo: ")
        #print("Pista: " + diccionario[0].)

