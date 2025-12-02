import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_masked_word(word, guessed_letters):
    return " ".join([letter if letter.upper() in guessed_letters or not letter.isalpha() else "_" for letter in word])

def play():
    clear_screen()
    print("--- JUEGO DEL AHORCADO ---")
    print("Jugador 1: Configuración del juego")
    
    secret_word = input("Ingresa la palabra o frase secreta: ").strip()
    description = input("Ingresa una descripción o pista: ").strip()
    
    while True:
        try:
            max_attempts = int(input("Ingresa el número máximo de intentos: "))
            if max_attempts > 0:
                break
            print("Por favor ingresa un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
            
    print("\nConfiguración completa. Pasando el turno al Jugador 2...")
    time.sleep(2)
    clear_screen()
    
    # Fake clear screen with newlines just in case
    print("\n" * 50)
    
    print("--- JUEGO DEL AHORCADO ---")
    print("Jugador 2: ¡Adivina la frase!")
    
    guessed_letters = set()
    attempts_left = max_attempts
    
    # Normalize secret word for checking (ignore case)
    secret_word_upper = secret_word.upper()
    # Set of letters to guess (ignoring spaces and non-alpha if desired, but let's keep it simple)
    letters_to_guess = set(c for c in secret_word_upper if c.isalnum())
    
    while attempts_left > 0:
        print(f"\nDescripción: {description}")
        print(f"Palabra: {get_masked_word(secret_word, guessed_letters)}")
        print(f"Intentos restantes: {attempts_left}")
        print(f"Letras usadas: {', '.join(sorted(guessed_letters))}")
        
        if all(c in guessed_letters for c in letters_to_guess):
            print("\n¡FELICIDADES! ¡Has adivinado la palabra!")
            print(f"La palabra era: {secret_word}")
            break
            
        guess = input("Ingresa una letra: ").strip().upper()
        
        if not guess or len(guess) != 1:
            print("Por favor ingresa una única letra.")
            continue
            
        if guess in guessed_letters:
            print(f"Ya usaste la letra '{guess}'. Intenta con otra.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in letters_to_guess:
            print(f"¡Bien! La letra '{guess}' está en la palabra.")
        else:
            print(f"Lo siento, la letra '{guess}' no está.")
            attempts_left -= 1
            
    if attempts_left == 0:
        print("\n¡JUEGO TERMINADO! Te has quedado sin intentos.")
        print(f"La palabra era: {secret_word}")
    
    input("\nPresiona Enter para volver al menú principal...")
