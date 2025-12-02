class RiverModel:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.left_bank = {'Lobo', 'Gallina', 'Maíz'}
        self.right_bank = set()
        self.boat_position = 'left' # 'left' or 'right'
        self.game_over = False
        self.won = False
        self.message = "Juego iniciado."

    def move(self, item):
        if self.game_over:
            return

        current_bank = self.left_bank if self.boat_position == 'left' else self.right_bank
        target_bank = self.right_bank if self.boat_position == 'left' else self.left_bank

        # Move item (if not None/Solo)
        if item:
            if item in current_bank:
                current_bank.remove(item)
                target_bank.add(item)
            else:
                self.message = "El ítem no está en la orilla actual."
                return

        # Move boat
        self.boat_position = 'right' if self.boat_position == 'left' else 'left'
        
        # Check state
        self.check_state()

    def check_state(self):
        # Check Win
        if len(self.left_bank) == 0 and len(self.right_bank) == 3:
            self.game_over = True
            self.won = True
            self.message = "¡Felicidades! Has cruzado a todos."
            return

        # Check Lose conditions on the bank WITHOUT the boat
        # The boat (and player) is now at self.boat_position.
        # So we check the OTHER bank.
        bank_to_check = self.left_bank if self.boat_position == 'right' else self.right_bank

        if 'Gallina' in bank_to_check and 'Lobo' in bank_to_check:
            self.game_over = True
            self.won = False
            self.message = "¡Oh no! El Lobo se comió a la Gallina."
        elif 'Gallina' in bank_to_check and 'Maíz' in bank_to_check:
            self.game_over = True
            self.won = False
            self.message = "¡Oh no! La Gallina se comió al Maíz."
        else:
            self.message = "Movimiento realizado."
