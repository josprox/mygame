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
        
        # Canvas for drawing Hangman
        self.canvas = tk.Canvas(self.game_frame, width=200, height=250, bg='white')
        self.canvas.pack(pady=10)
        
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

    def draw_hangman(self, attempts_left, max_attempts):
        self.canvas.delete("all")
        # Draw gallows
        self.canvas.create_line(50, 230, 150, 230, width=3) # Base
        self.canvas.create_line(100, 230, 100, 50, width=3) # Pole
        self.canvas.create_line(100, 50, 150, 50, width=3)  # Top
        self.canvas.create_line(150, 50, 150, 80, width=3)  # Rope
        
        errors = max_attempts - attempts_left
        
        # Calculate steps based on max_attempts (simplified for standard 6 parts)
        # If max_attempts is different, we map errors to parts.
        # Let's assume standard 6 parts for the drawing, and map progress.
        
        # Parts: Head, Body, Left Arm, Right Arm, Left Leg, Right Leg
        # We show parts based on percentage of errors? Or just map 1-6.
        # Let's stick to standard 6 parts. If user sets 10 attempts, we draw slowly?
        # For simplicity, let's draw based on ratio or just map to 6 stages.
        
        stage = int((errors / max_attempts) * 6) if max_attempts > 0 else 0
        if errors > 0 and stage == 0: stage = 1 # Show at least something if error
        
        if stage >= 1: # Head
            self.canvas.create_oval(130, 80, 170, 120, width=3)
        if stage >= 2: # Body
            self.canvas.create_line(150, 120, 150, 180, width=3)
        if stage >= 3: # Left Arm
            self.canvas.create_line(150, 140, 130, 160, width=3)
        if stage >= 4: # Right Arm
            self.canvas.create_line(150, 140, 170, 160, width=3)
        if stage >= 5: # Left Leg
            self.canvas.create_line(150, 180, 130, 210, width=3)
        if stage >= 6: # Right Leg
            self.canvas.create_line(150, 180, 170, 210, width=3)

    def update_ui(self, masked_word, attempts, description, game_over=False):
        self.word_label.config(text=masked_word)
        self.status_label.config(text=f"Intentos restantes: {attempts}")
        self.info_label.config(text=f"Pista: {description}")
        
        # We need max_attempts to draw correctly. 
        # Since we don't store it in view, we might need to ask controller or pass it.
        # For now, let's assume standard 6 or get it from controller if possible.
        # Better: Update update_ui signature in controller to pass max_attempts.
        # Or just use attempts_left and assume max is attempts_left + errors? No.
        # I'll update the controller to pass max_attempts.
        
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
