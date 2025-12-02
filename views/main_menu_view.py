import tkinter as tk
from tkinter import ttk

class MainMenuView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Title
        title_label = ttk.Label(self, text="Colección de Juegos Python", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=40)
        
        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="El Ahorcado", command=lambda: controller.show_game("hangman")).pack(fill='x', pady=10, ipadx=20, ipady=5)
        ttk.Button(btn_frame, text="Cartas Mágicas", command=lambda: controller.show_game("magic_cards")).pack(fill='x', pady=10, ipadx=20, ipady=5)
        ttk.Button(btn_frame, text="El Río", command=lambda: controller.show_game("river")).pack(fill='x', pady=10, ipadx=20, ipady=5)
        ttk.Button(btn_frame, text="Salir", command=parent.quit).pack(fill='x', pady=10, ipadx=20, ipady=5)
