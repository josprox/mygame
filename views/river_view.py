from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QFrame, QListWidget, QGroupBox, QMessageBox)
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QBrush, QFont

class RiverCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(600, 300)
        self.left_items = []
        self.right_items = []
        self.boat_pos = 'left'

    def update_state(self, left_items, right_items, boat_pos):
        self.left_items = left_items
        self.right_items = right_items
        self.boat_pos = boat_pos
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw River and Banks
        painter.fillRect(QRect(0, 0, 150, 300), QColor("lightgreen")) # Left Bank
        painter.fillRect(QRect(150, 0, 300, 300), QColor("skyblue"))  # River
        painter.fillRect(QRect(450, 0, 150, 300), QColor("lightgreen")) # Right Bank
        
        # Draw Boat
        boat_x = 160 if self.boat_pos == 'left' else 340
        boat_y = 100
        painter.fillRect(QRect(boat_x, boat_y, 100, 50), QColor("brown"))
        painter.setPen(QColor("white"))
        painter.drawText(QRect(boat_x, boat_y, 100, 50), Qt.AlignCenter, "BARCA")
        
        # Helper to draw items
        def draw_item(item, x, y):
            color = QColor("gray")
            if item == 'Lobo': color = QColor("gray")
            elif item == 'Gallina': color = QColor("white")
            elif item == 'Maíz': color = QColor("yellow")
            
            painter.setBrush(QBrush(color))
            painter.setPen(QColor("black"))
            painter.drawEllipse(x, y, 40, 40)
            
            painter.setPen(QColor("black"))
            painter.drawText(QRect(x, y, 40, 40), Qt.AlignCenter, item[0])
            painter.drawText(x, y + 55, item)

        # Draw items on banks
        for i, item in enumerate(self.left_items):
            draw_item(item, 50, 50 + (i * 60))
            
        for i, item in enumerate(self.right_items):
            draw_item(item, 500, 50 + (i * 60))

class RiverView(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        layout = QVBoxLayout(self)
        
        title = QLabel("El Río (Lobo, Gallina, Maíz)")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        self.status_label = QLabel("Juego iniciado.")
        self.status_label.setProperty("class", "subtitle")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Canvas
        self.canvas = RiverCanvas()
        layout.addWidget(self.canvas, 0, Qt.AlignCenter)
        
        # Controls
        controls_group = QGroupBox("Controles")
        controls_layout = QHBoxLayout(controls_group)
        
        btn_wolf = QPushButton("Mover Lobo")
        btn_wolf.clicked.connect(lambda: self.controller.move_item("Lobo"))
        controls_layout.addWidget(btn_wolf)
        
        btn_chicken = QPushButton("Mover Gallina")
        btn_chicken.clicked.connect(lambda: self.controller.move_item("Gallina"))
        controls_layout.addWidget(btn_chicken)
        
        btn_corn = QPushButton("Mover Maíz")
        btn_corn.clicked.connect(lambda: self.controller.move_item("Maíz"))
        controls_layout.addWidget(btn_corn)
        
        btn_boat = QPushButton("Mover Barca (Solo)")
        btn_boat.clicked.connect(lambda: self.controller.move_item(None))
        controls_layout.addWidget(btn_boat)
        
        layout.addWidget(controls_group)
        
        bottom_layout = QHBoxLayout()
        btn_reset = QPushButton("Reiniciar")
        btn_reset.clicked.connect(self.controller.reset_game)
        bottom_layout.addWidget(btn_reset)
        
        btn_back = QPushButton("Volver al Menú")
        btn_back.clicked.connect(self.controller.go_back)
        bottom_layout.addWidget(btn_back)
        
        layout.addLayout(bottom_layout)

    def update_ui(self, left_items, right_items, boat_pos, message):
        self.status_label.setText(message)
        self.canvas.update_state(left_items, right_items, boat_pos)
