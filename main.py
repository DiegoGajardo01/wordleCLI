import random

bcl = True

with open("palabras.txt", encoding="utf-8") as f:
    palabras = [line.strip() for line in f if len(line.strip()) == 5]
    
word = random.choice(palabras)

print("¡¡Bienvenido al worle en CLI!!\n\n")

def evaluar_palabra(intento, palabra_objetivo):
    buenas = 0
    aciertos = 0
    usadas = []

    for i in range(len(intento)):
        if i < len(palabra_objetivo) and intento[i] == palabra_objetivo[i]:
            buenas += 1
            usadas.append(i)

    for i in range(len(intento)):
        if intento[i] in palabra_objetivo:
            # Ya fue contada como buena
            if i < len(palabra_objetivo) and intento[i] == palabra_objetivo[i]:
                continue

            for j in range(len(palabra_objetivo)):
                if intento[i] == palabra_objetivo[j] and j not in usadas and intento[j] != palabra_objetivo[j]:
                    aciertos += 1
                    usadas.append(j)
                    break

    print(f"Buenas: {buenas}, Aciertos: {aciertos}")


while bcl: 
    print("-" * len(word))
    wordInput = input("Ingresa una palabra: ").lower()

    if len(wordInput) != len(word):
        print(f"Intenta con una palabra de {len(word)} letras\n")
    else: 
        evaluar_palabra(wordInput, word)
        if wordInput == word:
            print(f"¡Felicidades! Adivinaste la {word}.")
            bcl = False