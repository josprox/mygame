from models.river_model import RiverModel
from views.river_view import RiverView
from PySide6.QtWidgets import QMessageBox

class RiverController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.model = RiverModel()
        self.view = RiverView(main_controller.window, self)

    def get_view(self):
        return self.view

    def start_game(self):
        self.model.reset_game()
        self.update_view()

    def reset_game(self):
        self.start_game()

    def move_item(self, item):
        self.model.move(item)
        self.update_view()
        
        if self.model.game_over:
            if self.model.won:
                QMessageBox.information(self.view, "¡Victoria!", self.model.message)
            else:
                QMessageBox.critical(self.view, "Game Over", self.model.message)
                self.reset_game()

    def update_view(self):
        self.view.update_ui(
            sorted(list(self.model.left_bank)), 
            sorted(list(self.model.right_bank)), 
            self.model.boat_position,
            self.model.message
        )

    def go_back(self):
        self.main_controller.show_menu()
