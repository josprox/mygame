from models.hangman_model import HangmanModel
from views.hangman_view import HangmanView
from PySide6.QtWidgets import QMessageBox

class HangmanController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.model = HangmanModel()
        self.view = HangmanView(main_controller.window, self) # Pass window as parent

    def get_view(self):
        return self.view

    def start_game(self, word, description, attempts):
        self.model.start_game(word, description, attempts)
        self.view.reset_keyboard()
        self.update_view()

    def guess_letter(self, letter):
        success, message = self.model.guess_letter(letter)
        
        self.view.disable_button(letter)
        
        if self.model.game_over:
            self.update_view()
            if self.model.won:
                QMessageBox.information(self.view, "¡Ganaste!", message)
            else:
                QMessageBox.information(self.view, "Perdiste", f"{message}\nLa palabra era: {self.model.secret_word}")
        else:
            self.update_view()

    def update_view(self):
        masked = self.model.get_masked_word()
        self.view.update_ui(masked, self.model.attempts_left, self.model.description, self.model.game_over)
        self.view.draw_hangman(self.model.attempts_left, self.model.max_attempts)

    def go_back(self):
        self.main_controller.show_menu()
