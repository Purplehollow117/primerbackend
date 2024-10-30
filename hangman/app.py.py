Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def elegir_palabra():
...     palabras = ['python', 'programacion', 'desarrollo', 'hangman', 'juego']
...     return random.choice(palabras)
... 
... def mostrar_estado(palabra, letras_adivinadas):
...     estado = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
...     return estado
... 
... def jugar_hangman():
...     palabra = elegir_palabra()
...     letras_adivinadas = set()
...     intentos = 6
... 
...     print("¡Bienvenido al juego de Hangman!")
... 
...     while intentos > 0:
...         print(f"\nPalabra: {mostrar_estado(palabra, letras_adivinadas)}")
...         print(f"Tienes {intentos} intentos restantes.")
...         print("Letras adivinadas:", ' '.join(sorted(letras_adivinadas)))
... 
...         letra = input("Adivina una letra: ").lower()
... 
...         if letra in letras_adivinadas:
...             print("Ya has adivinado esa letra.")
...             continue
... 
...         letras_adivinadas.add(letra)
... 
...         if letra in palabra:
...             print("¡Correcto!")
...         else:
...             intentos -= 1
...             print("Incorrecto!")
... 
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
            break
    else:
        print(f"Te quedaste sin intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_hangman()
