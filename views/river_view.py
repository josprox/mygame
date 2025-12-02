import tkinter as tk
from tkinter import ttk

class RiverView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.create_ui()

    def create_ui(self):
        ttk.Label(self, text="El Río (Lobo, Gallina, Maíz)", font=("Helvetica", 18)).pack(pady=10)
        
        self.status_label = ttk.Label(self, text="Juego iniciado.", font=("Helvetica", 10, "italic"))
        self.status_label.pack(pady=5)
        
        game_area = ttk.Frame(self)
        game_area.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left Bank
        left_frame = ttk.LabelFrame(game_area, text="Orilla Izquierda")
        left_frame.pack(side='left', fill='both', expand=True, padx=5)
        self.left_list = tk.Listbox(left_frame, height=10)
        self.left_list.pack(fill='both', expand=True, padx=5, pady=5)
        ttk.Button(left_frame, text="Mover a la Barca ->", command=self.move_from_left).pack(pady=5)
        
        # River / Boat
        river_frame = ttk.Frame(game_area)
        river_frame.pack(side='left', fill='y', padx=10)
        self.boat_label = ttk.Label(river_frame, text="[ BARCA ]\n(Izquierda)", font=("Courier", 12, "bold"), justify='center')
        self.boat_label.pack(pady=50)
        ttk.Button(river_frame, text="Cruzar Río (Solo)", command=lambda: self.controller.move_item(None)).pack()
        
        # Right Bank
        right_frame = ttk.LabelFrame(game_area, text="Orilla Derecha")
        right_frame.pack(side='left', fill='both', expand=True, padx=5)
        self.right_list = tk.Listbox(right_frame, height=10)
        self.right_list.pack(fill='both', expand=True, padx=5, pady=5)
        ttk.Button(right_frame, text="<- Mover a la Barca", command=self.move_from_right).pack(pady=5)
        
        ttk.Button(self, text="Reiniciar", command=self.controller.reset_game).pack(pady=5)
        ttk.Button(self, text="Volver al Menú", command=self.controller.go_back).pack(pady=5)

    def update_ui(self, left_items, right_items, boat_pos, message):
        self.left_list.delete(0, tk.END)
        for item in left_items:
            self.left_list.insert(tk.END, item)
            
        self.right_list.delete(0, tk.END)
        for item in right_items:
            self.right_list.insert(tk.END, item)
            
        boat_text = "[ BARCA ]\n(Izquierda)" if boat_pos == 'left' else "[ BARCA ]\n(Derecha)"
        self.boat_label.config(text=boat_text)
        self.status_label.config(text=message)

    def move_from_left(self):
        selection = self.left_list.curselection()
        if selection:
            item = self.left_list.get(selection[0])
            self.controller.move_item(item)

    def move_from_right(self):
        selection = self.right_list.curselection()
        if selection:
            item = self.right_list.get(selection[0])
            self.controller.move_item(item)
