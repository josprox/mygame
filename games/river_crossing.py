import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_state(left_bank, right_bank, boat_position):
    """
    Returns:
    - 0: Game continues
    - 1: Win
    - -1: Lose (Wolf eats Chicken)
    - -2: Lose (Chicken eats Corn)
    """
    # Check Win
    if len(left_bank) == 0 and len(right_bank) == 3:
        return 1
    
    # Check Lose conditions on the bank WITHOUT the boat
    # If boat is on left, check right bank for conflicts (though right bank is safe if boat is there? No, boat is with player)
    # The player is ALWAYS with the boat. So we check the bank where the boat is NOT.
    
    bank_to_check = left_bank if boat_position == 'right' else right_bank
    
    if 'Gallina' in bank_to_check and 'Lobo' in bank_to_check:
        return -1
    if 'Gallina' in bank_to_check and 'Maíz' in bank_to_check:
        return -2
        
    return 0

def play():
    left_bank = {'Lobo', 'Gallina', 'Maíz'}
    right_bank = set()
    boat_position = 'left' # 'left' or 'right'
    
    while True:
        clear_screen()
        print("--- EL RÍO (Lobo, Gallina, Maíz) ---")
        print("Objetivo: Cruzar todo al otro lado.")
        print("Reglas:")
        print("1. El Lobo se come a la Gallina si se quedan solos.")
        print("2. La Gallina se come al Maíz si se quedan solos.")
        print("3. La barca solo puede llevarte a ti y a una cosa más.")
        print("----------------------------------------")
        
        print(f"\nOrilla Izquierda: {', '.join(left_bank)}")
        print(f"Orilla Derecha:   {', '.join(right_bank)}")
        
        boat_side_str = "Izquierda" if boat_position == 'left' else "Derecha"
        print(f"\nLa barca está en la orilla: {boat_side_str}")
        
        # Check game state
        status = check_state(left_bank, right_bank, boat_position)
        if status == 1:
            print("\n¡FELICIDADES! ¡Has cruzado a todos a salvo!")
            break
        elif status == -1:
            print("\n¡OH NO! El Lobo se ha comido a la Gallina.")
            print("Juego Terminado.")
            break
        elif status == -2:
            print("\n¡OH NO! La Gallina se ha comido al Maíz.")
            print("Juego Terminado.")
            break
            
        # Actions
        current_bank = left_bank if boat_position == 'left' else right_bank
        
        print("\n¿Qué quieres hacer?")
        print("0. Cruzar solo")
        
        items = list(current_bank)
        for i, item in enumerate(items):
            print(f"{i+1}. Cruzar con {item}")
            
        choice = input("\nElige una opción: ")
        
        if choice == '0':
            boat_position = 'right' if boat_position == 'left' else 'left'
            continue
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                item_to_move = items[idx]
                
                # Move item
                if boat_position == 'left':
                    left_bank.remove(item_to_move)
                    right_bank.add(item_to_move)
                    boat_position = 'right'
                else:
                    right_bank.remove(item_to_move)
                    left_bank.add(item_to_move)
                    boat_position = 'left'
            else:
                print("Opción inválida.")
                time.sleep(1)
        except ValueError:
            print("Entrada inválida.")
            time.sleep(1)

    input("\nPresiona Enter para volver al menú principal...")
