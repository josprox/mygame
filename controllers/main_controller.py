from PySide6.QtWidgets import QMainWindow, QStackedWidget
from views.main_menu_view import MainMenuView
from controllers.hangman_controller import HangmanController
from controllers.magic_cards_controller import MagicCardsController
from controllers.river_controller import RiverController

class MainController:
    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("Colección de Juegos Python")
        self.window.resize(800, 600)
        
        self.stacked_widget = QStackedWidget()
        self.window.setCentralWidget(self.stacked_widget)
        
        # Views
        self.main_menu = MainMenuView(self.window, self)
        self.stacked_widget.addWidget(self.main_menu)
        
        # Initialize controllers
        self.hangman_controller = HangmanController(self)
        self.stacked_widget.addWidget(self.hangman_controller.get_view())
        
        self.magic_cards_controller = MagicCardsController(self)
        self.stacked_widget.addWidget(self.magic_cards_controller.get_view())
        
        self.river_controller = RiverController(self)
        self.stacked_widget.addWidget(self.river_controller.get_view())
        
        self.show_menu()

    def show_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def show_game(self, game_name):
        if game_name == "hangman":
            self.stacked_widget.setCurrentWidget(self.hangman_controller.get_view())
            self.hangman_controller.view.show_setup()
        elif game_name == "magic_cards":
            self.stacked_widget.setCurrentWidget(self.magic_cards_controller.get_view())
            self.magic_cards_controller.view.show_intro()
        elif game_name == "river":
            self.stacked_widget.setCurrentWidget(self.river_controller.get_view())
            self.river_controller.start_game()

    def run(self):
        self.window.show()
