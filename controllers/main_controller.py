import tkinter as tk
from views.main_menu_view import MainMenuView
from controllers.hangman_controller import HangmanController
from controllers.magic_cards_controller import MagicCardsController
from controllers.river_controller import RiverController

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Colección de Juegos Python")
        self.root.geometry("800x600")
        
        self.main_menu = MainMenuView(self.root, self)
        
        # Initialize controllers
        self.hangman_controller = HangmanController(self)
        self.magic_cards_controller = MagicCardsController(self)
        self.river_controller = RiverController(self)
        
        self.current_view = None
        self.show_menu()

    def show_menu(self):
        if self.current_view:
            self.current_view.pack_forget()
        self.main_menu.pack(fill='both', expand=True)
        self.current_view = self.main_menu

    def show_game(self, game_name):
        if self.current_view:
            self.current_view.pack_forget()
            
        if game_name == "hangman":
            self.current_view = self.hangman_controller.get_view()
            # Reset/Setup hangman if needed? The view handles setup screen.
            self.hangman_controller.view.show_setup()
        elif game_name == "magic_cards":
            self.current_view = self.magic_cards_controller.get_view()
            self.magic_cards_controller.view.show_intro()
        elif game_name == "river":
            self.current_view = self.river_controller.get_view()
            self.river_controller.start_game()
            
        self.current_view.pack(fill='both', expand=True)

    def run(self):
        self.root.mainloop()
