import tkinter as tk
from tkinter import ttk, messagebox

class HangmanView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.setup_frame = ttk.Frame(self)
        self.game_frame = ttk.Frame(self)
        
        self.create_setup_ui()
        self.create_game_ui()
        
        self.show_setup()

    def show_setup(self):
        self.game_frame.pack_forget()
        self.setup_frame.pack(fill='both', expand=True)
        # Clear inputs
        self.word_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.attempts_entry.delete(0, tk.END)
        self.attempts_entry.insert(0, "6")

    def show_game(self):
        self.setup_frame.pack_forget()
        self.game_frame.pack(fill='both', expand=True)

    def create_setup_ui(self):
        ttk.Label(self.setup_frame, text="Configuración del Ahorcado", font=("Helvetica", 18)).pack(pady=20)
        
        form_frame = ttk.Frame(self.setup_frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Palabra Secreta:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.word_entry = ttk.Entry(form_frame, show="*")
        self.word_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Pista/Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.desc_entry = ttk.Entry(form_frame)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Intentos:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.attempts_entry = ttk.Entry(form_frame)
        self.attempts_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.setup_frame, text="Iniciar Juego", command=self.start_game_action).pack(pady=20)
        ttk.Button(self.setup_frame, text="Volver al Menú", command=self.controller.go_back).pack()

    def create_game_ui(self):
        top_frame = ttk.Frame(self.game_frame)
        top_frame.pack(fill='x', pady=10)
        ttk.Button(top_frame, text="Rendirse / Volver", command=self.controller.go_back).pack(side='left', padx=10)
        
        self.info_label = ttk.Label(self.game_frame, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=5)
        
        self.word_label = ttk.Label(self.game_frame, text="_ _ _ _ _", font=("Courier", 24, "bold"))
        self.word_label.pack(pady=20)
        
        self.status_label = ttk.Label(self.game_frame, text="Intentos restantes: 6")
        self.status_label.pack(pady=5)
        
        # Keyboard
        self.keyboard_frame = ttk.Frame(self.game_frame)
        self.keyboard_frame.pack(pady=20)
        
        self.letter_buttons = {}
        letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        row = 0
        col = 0
        for char in letters:
            btn = ttk.Button(self.keyboard_frame, text=char, width=4, command=lambda c=char: self.guess_action(c))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.letter_buttons[char] = btn
            col += 1
            if col > 8:
                col = 0
                row += 1

    def start_game_action(self):
        word = self.word_entry.get().strip()
        desc = self.desc_entry.get().strip()
        try:
            attempts = int(self.attempts_entry.get())
            if not word:
                messagebox.showerror("Error", "La palabra no puede estar vacía.")
                return
            if attempts < 1:
                messagebox.showerror("Error", "Los intentos deben ser mayor a 0.")
                return
            
            self.controller.start_game(word, desc, attempts)
            self.show_game()
            
        except ValueError:
            messagebox.showerror("Error", "Intentos debe ser un número.")

    def guess_action(self, char):
        self.controller.guess_letter(char)

    def update_ui(self, masked_word, attempts, description, game_over=False):
        self.word_label.config(text=masked_word)
        self.status_label.config(text=f"Intentos restantes: {attempts}")
        self.info_label.config(text=f"Pista: {description}")
        
        if game_over:
            for btn in self.letter_buttons.values():
                btn.state(['disabled'])
        else:
            # Enable all buttons initially, controller logic handles disabling used ones? 
            # Actually, view should disable clicked ones.
            pass

    def disable_button(self, char):
        if char in self.letter_buttons:
            self.letter_buttons[char].state(['disabled'])
            
    def reset_keyboard(self):
        for btn in self.letter_buttons.values():
            btn.state(['!disabled'])
