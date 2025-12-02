class MagicCardsModel:
    def __init__(self):
        self.current_card_index = 0
        self.accumulated_number = 0
        self.total_cards = 5

    def reset_game(self):
        self.current_card_index = 0
        self.accumulated_number = 0

    def get_current_card_numbers(self):
        if self.current_card_index >= self.total_cards:
            return []
        
        card_numbers = []
        for i in range(1, 32):
            if (i >> self.current_card_index) & 1:
                card_numbers.append(i)
        return card_numbers

    def process_answer(self, is_yes):
        if is_yes:
            self.accumulated_number += (1 << self.current_card_index)
        
        self.current_card_index += 1
        
        return self.current_card_index >= self.total_cards

    def get_result(self):
        return self.accumulated_number
