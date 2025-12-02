from models.magic_cards_model import MagicCardsModel
from views.magic_cards_view import MagicCardsView

class MagicCardsController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.model = MagicCardsModel()
        self.view = MagicCardsView(main_controller.root, self)

    def get_view(self):
        return self.view

    def start_game(self):
        self.model.reset_game()
        self.update_card()
        self.view.show_game()

    def update_card(self):
        numbers = self.model.get_current_card_numbers()
        self.view.update_card(self.model.current_card_index, numbers)

    def answer(self, is_yes):
        finished = self.model.process_answer(is_yes)
        if finished:
            result = self.model.get_result()
            self.view.show_result(result)
        else:
            self.update_card()

    def go_back(self):
        self.main_controller.show_menu()
