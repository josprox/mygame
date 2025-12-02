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
        
        # Canvas for the visual scene
        self.canvas = tk.Canvas(self, width=600, height=300, bg='skyblue')
        self.canvas.pack(pady=10)
        
        # Control Buttons Frame
        controls_frame = ttk.Frame(self)
        controls_frame.pack(pady=10)
        
        ttk.Button(controls_frame, text="Mover Lobo", command=lambda: self.controller.move_item("Lobo")).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Mover Gallina", command=lambda: self.controller.move_item("Gallina")).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Mover Maíz", command=lambda: self.controller.move_item("Maíz")).pack(side='left', padx=5)
        ttk.Button(controls_frame, text="Mover Barca (Solo)", command=lambda: self.controller.move_item(None)).pack(side='left', padx=5)
        
        ttk.Button(self, text="Reiniciar", command=self.controller.reset_game).pack(pady=5)
        ttk.Button(self, text="Volver al Menú", command=self.controller.go_back).pack(pady=5)

    def update_ui(self, left_items, right_items, boat_pos, message):
        self.status_label.config(text=message)
        self.canvas.delete("all")
        
        # Draw Banks
        self.canvas.create_rectangle(0, 0, 150, 300, fill='lightgreen', outline='') # Left Bank
        self.canvas.create_rectangle(450, 0, 600, 300, fill='lightgreen', outline='') # Right Bank
        
        # Draw River
        self.canvas.create_rectangle(150, 0, 450, 300, fill='skyblue', outline='')
        
        # Draw Boat
        boat_x = 160 if boat_pos == 'left' else 340
        boat_y = 100
        self.canvas.create_rectangle(boat_x, boat_y, boat_x + 100, boat_y + 50, fill='brown', outline='black')
        self.canvas.create_text(boat_x + 50, boat_y + 25, text="BARCA", fill='white')
        
        # Draw Items
        # Helper to draw item
        def draw_item(item, location, index):
            # location: 'left', 'right'
            # index: position offset
            x = 50 if location == 'left' else 500
            y = 50 + (index * 60)
            
            color = 'gray'
            if item == 'Lobo': color = 'gray'
            elif item == 'Gallina': color = 'white'
            elif item == 'Maíz': color = 'yellow'
            
            self.canvas.create_oval(x, y, x+40, y+40, fill=color, outline='black')
            self.canvas.create_text(x+20, y+20, text=item[0], font=("Arial", 14, "bold")) # Initial
            self.canvas.create_text(x+20, y+50, text=item)

        # Draw items on banks
        for i, item in enumerate(left_items):
            draw_item(item, 'left', i)
            
        for i, item in enumerate(right_items):
            draw_item(item, 'right', i)
