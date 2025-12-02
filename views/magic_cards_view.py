import tkinter as tk
from tkinter import ttk

class MagicCardsView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.intro_frame = ttk.Frame(self)
        self.game_frame = ttk.Frame(self)
        self.result_frame = ttk.Frame(self)
        
        self.create_intro_ui()
        self.create_game_ui()
        self.create_result_ui()
        
        self.show_intro()

    def show_intro(self):
        self.game_frame.pack_forget()
        self.result_frame.pack_forget()
        self.intro_frame.pack(fill='both', expand=True)

    def show_game(self):
        self.intro_frame.pack_forget()
        self.result_frame.pack_forget()
        self.game_frame.pack(fill='both', expand=True)

    def show_result(self, number):
        self.intro_frame.pack_forget()
        self.game_frame.pack_forget()
        self.result_label.config(text=f"¡Tu número es el {number}!")
        self.result_frame.pack(fill='both', expand=True)

    def create_intro_ui(self):
        ttk.Label(self.intro_frame, text="Cartas Mágicas", font=("Helvetica", 24)).pack(pady=30)
        ttk.Label(self.intro_frame, text="Piensa en un número del 1 al 31.", font=("Helvetica", 14)).pack(pady=10)
        ttk.Button(self.intro_frame, text="¡Estoy listo!", command=self.controller.start_game).pack(pady=20)
        ttk.Button(self.intro_frame, text="Volver", command=self.controller.go_back).pack()

    def create_game_ui(self):
        self.card_label = ttk.Label(self.game_frame, text="Carta X", font=("Helvetica", 16))
        self.card_label.pack(pady=20)
        
        self.numbers_text = tk.Text(self.game_frame, height=8, width=30, font=("Courier", 14))
        self.numbers_text.pack(pady=10)
        self.numbers_text.config(state='disabled')
        
        ttk.Label(self.game_frame, text="¿Está tu número en esta carta?").pack(pady=10)
        
        btn_frame = ttk.Frame(self.game_frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="SÍ", command=lambda: self.controller.answer(True)).pack(side='left', padx=20)
        ttk.Button(btn_frame, text="NO", command=lambda: self.controller.answer(False)).pack(side='left', padx=20)

    def create_result_ui(self):
        self.result_label = ttk.Label(self.result_frame, text="", font=("Helvetica", 30, "bold"))
        self.result_label.pack(pady=50)
        ttk.Button(self.result_frame, text="Jugar de nuevo", command=self.show_intro).pack(pady=10)
        ttk.Button(self.result_frame, text="Volver al Menú", command=self.controller.go_back).pack(pady=10)

    def update_card(self, index, numbers):
        self.card_label.config(text=f"Carta {index + 1}")
        
        # Format numbers nicely
        content = ""
        for i in range(0, len(numbers), 4):
            row = numbers[i:i+4]
            content += " ".join(f"{num:^6}" for num in row) + "\n"
            
        self.numbers_text.config(state='normal')
        self.numbers_text.delete(1.0, tk.END)
        self.numbers_text.insert(tk.END, content)
        self.numbers_text.config(state='disabled')
