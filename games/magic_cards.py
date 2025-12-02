import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_card(bit_index):
    """Generates a list of numbers between 1 and 31 that have the bit_index set."""
    card_numbers = []
    for i in range(1, 32):
        if (i >> bit_index) & 1:
            card_numbers.append(i)
    return card_numbers

def print_card(numbers):
    print("+------------------------------------------------+")
    # Print numbers in rows of 4
    for i in range(0, len(numbers), 4):
        row = numbers[i:i+4]
        row_str = "".join(f"{num:^12}" for num in row)
        print(f"|{row_str}|")
    print("+------------------------------------------------+")

def play():
    clear_screen()
    print("--- CARTAS MÁGICAS ---")
    print("Piensa en un número del 1 al 31.")
    print("No me lo digas, solo mantenlo en tu mente.")
    input("Presiona Enter cuando estés listo...")
    
    result = 0
    
    for i in range(5):
        clear_screen()
        print(f"--- CARTA {i+1} ---")
        card_numbers = generate_card(i)
        print_card(card_numbers)
        
        while True:
            response = input("\n¿Está tu número en esta carta? (s/n): ").lower().strip()
            if response in ['s', 'si', 'y', 'yes']:
                result += (1 << i) # Add 2^i
                break
            elif response in ['n', 'no']:
                break
            else:
                print("Por favor responde 's' o 'n'.")
    
    clear_screen()
    print("--- RESULTADO ---")
    print("Leyendo tu mente...")
    time.sleep(2)
    
    if result == 0:
        print("Mmm... parece que no elegiste ningún número o te equivocaste en las respuestas.")
        print("Recuerda que el número debe ser entre 1 y 31.")
    else:
        print(f"¡Tu número es el {result}!")
        
    input("\nPresiona Enter para volver al menú principal...")
