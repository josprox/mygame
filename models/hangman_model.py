class HangmanModel:
    def __init__(self):
        self.secret_word = ""
        self.description = ""
        self.max_attempts = 6
        self.attempts_left = 6
        self.guessed_letters = set()
        self.game_over = False
        self.won = False

    def start_game(self, word, description, max_attempts):
        self.secret_word = word.upper()
        self.description = description
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.guessed_letters = set()
        self.game_over = False
        self.won = False

    def guess_letter(self, letter):
        if self.game_over:
            return False, "El juego ha terminado."

        letter = letter.upper()
        if not letter.isalpha() or len(letter) != 1:
            return False, "Entrada inválida."

        if letter in self.guessed_letters:
            return False, f"Ya usaste la letra '{letter}'."

        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            if self.check_win():
                self.game_over = True
                self.won = True
                return True, "¡Correcto! Has ganado."
            return True, "¡Correcto!"
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.game_over = True
                return True, "Incorrecto. Has perdido."
            return True, "Incorrecto."

    def get_masked_word(self):
        return " ".join([letter if letter in self.guessed_letters or not letter.isalpha() else "_" for letter in self.secret_word])

    def check_win(self):
        # Check if all alphabetic characters in secret_word are in guessed_letters
        return all(letter in self.guessed_letters for letter in self.secret_word if letter.isalpha())
