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
        # Card Container (Styled Frame)
        self.card_frame = tk.Frame(self.game_frame, bg="white", bd=2, relief="raised")
        self.card_frame.pack(pady=20, padx=50, ipadx=20, ipady=20)
        
        self.card_label = tk.Label(self.card_frame, text="Carta X", font=("Times New Roman", 18, "bold"), bg="white", fg="darkred")
        self.card_label.pack(pady=10)
        
        # Numbers display
        self.numbers_label = tk.Label(self.card_frame, text="", font=("Courier New", 16), bg="white", justify="center")
        self.numbers_label.pack(pady=10)
        
        ttk.Label(self.game_frame, text="¿Está tu número en esta carta?").pack(pady=10)
        
        btn_frame = ttk.Frame(self.game_frame)
        btn_frame.pack(pady=10)
        
        # Styled Buttons (using ttk styles if possible, or just standard buttons for color)
        yes_btn = tk.Button(btn_frame, text="SÍ", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=10, command=lambda: self.controller.answer(True))
        yes_btn.pack(side='left', padx=20)
        
        no_btn = tk.Button(btn_frame, text="NO", font=("Helvetica", 12, "bold"), bg="#F44336", fg="white", width=10, command=lambda: self.controller.answer(False))
        no_btn.pack(side='left', padx=20)

    def create_result_ui(self):
        self.result_label = ttk.Label(self.result_frame, text="", font=("Helvetica", 30, "bold"))
        self.result_label.pack(pady=50)
        ttk.Button(self.result_frame, text="Jugar de nuevo", command=self.show_intro).pack(pady=10)
        ttk.Button(self.result_frame, text="Volver al Menú", command=self.controller.go_back).pack(pady=10)

    def update_card(self, index, numbers):
        self.card_label.config(text=f"CARTA {index + 1}")
        
        # Format numbers nicely
        content = ""
        for i in range(0, len(numbers), 4):
            row = numbers[i:i+4]
            content += " ".join(f"{num:^4}" for num in row) + "\n"
            
        self.numbers_label.config(text=content)
