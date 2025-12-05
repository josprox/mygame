from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QMessageBox, QGridLayout, QFrame)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPainter, QPen, QColor, QFont

class HangmanCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(220, 260)
        self.attempts_left = 6
        self.max_attempts = 6

    def update_state(self, attempts_left, max_attempts):
        self.attempts_left = attempts_left
        self.max_attempts = max_attempts
        self.update() # Trigger paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(QColor("white"))
        pen.setWidth(3)
        painter.setPen(pen)
        
        # Draw Gallows
        painter.drawLine(50, 230, 150, 230) # Base
        painter.drawLine(100, 230, 100, 50) # Pole
        painter.drawLine(100, 50, 150, 50)  # Top
        painter.drawLine(150, 50, 150, 80)  # Rope
        
        errors = self.max_attempts - self.attempts_left
        stage = int((errors / self.max_attempts) * 6) if self.max_attempts > 0 else 0
        if errors > 0 and stage == 0: stage = 1
        
        if stage >= 1: # Head
            painter.drawEllipse(130, 80, 40, 40)
        if stage >= 2: # Body
            painter.drawLine(150, 120, 150, 180)
        if stage >= 3: # Left Arm
            painter.drawLine(150, 140, 130, 160)
        if stage >= 4: # Right Arm
            painter.drawLine(150, 140, 170, 160)
        if stage >= 5: # Left Leg
            painter.drawLine(150, 180, 130, 210)
        if stage >= 6: # Right Leg
            painter.drawLine(150, 180, 170, 210)

class HangmanView(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.layout = QVBoxLayout(self)
        
        self.setup_widget = QWidget()
        self.game_widget = QWidget()
        
        self.create_setup_ui()
        self.create_game_ui()
        
        self.layout.addWidget(self.setup_widget)
        self.layout.addWidget(self.game_widget)
        
        self.show_setup()

    def show_setup(self):
        self.game_widget.hide()
        self.setup_widget.show()
        self.word_entry.clear()
        self.desc_entry.clear()
        self.attempts_entry.setText("6")

    def show_game(self):
        self.setup_widget.hide()
        self.game_widget.show()

    def create_setup_ui(self):
        layout = QVBoxLayout(self.setup_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Configuración del Ahorcado")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        form_layout = QGridLayout()
        form_layout.setSpacing(10)
        
        form_layout.addWidget(QLabel("Palabra Secreta:"), 0, 0)
        self.word_entry = QLineEdit()
        self.word_entry.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.word_entry, 0, 1)
        
        form_layout.addWidget(QLabel("Pista/Descripción:"), 1, 0)
        self.desc_entry = QLineEdit()
        form_layout.addWidget(self.desc_entry, 1, 1)
        
        form_layout.addWidget(QLabel("Intentos:"), 2, 0)
        self.attempts_entry = QLineEdit()
        form_layout.addWidget(self.attempts_entry, 2, 1)
        
        layout.addLayout(form_layout)
        
        btn_start = QPushButton("Iniciar Juego")
        btn_start.setProperty("class", "accent")
        btn_start.clicked.connect(self.start_game_action)
        layout.addWidget(btn_start)
        
        btn_back = QPushButton("Volver al Menú")
        btn_back.clicked.connect(self.controller.go_back)
        layout.addWidget(btn_back)

    def create_game_ui(self):
        layout = QVBoxLayout(self.game_widget)
        
        top_bar = QHBoxLayout()
        btn_giveup = QPushButton("Rendirse / Volver")
        btn_giveup.clicked.connect(self.controller.go_back)
        top_bar.addWidget(btn_giveup)
        top_bar.addStretch()
        layout.addLayout(top_bar)
        
        # Canvas
        self.canvas = HangmanCanvas()
        layout.addWidget(self.canvas, 0, Qt.AlignCenter)
        
        self.info_label = QLabel("")
        self.info_label.setProperty("class", "subtitle")
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        
        self.word_label = QLabel("_ _ _ _ _")
        self.word_label.setFont(QFont("Courier New", 24, QFont.Bold))
        self.word_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.word_label)
        
        self.status_label = QLabel("Intentos restantes: 6")
        self.status_label.setFont(QFont("Courier New", 18, QFont.Bold))
        self.status_label.setContentsMargins(0, 10, 0, 0)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Keyboard
        self.keyboard_layout = QGridLayout()
        self.keyboard_layout.setContentsMargins(0, 10, 0, 0)
        self.keyboard_layout.setSpacing(5)
        layout.addLayout(self.keyboard_layout)
        
        self.letter_buttons = {}
        letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        row = 0
        col = 0
        for char in letters:
            btn = QPushButton(char)
            btn.setFixedSize(60, 60)
            btn.clicked.connect(lambda checked=False, c=char: self.guess_action(c))
            self.keyboard_layout.addWidget(btn, row, col)
            self.letter_buttons[char] = btn
            col += 1
            if col > 8:
                col = 0
                row += 1

    def start_game_action(self):
        word = self.word_entry.text().strip()
        desc = self.desc_entry.text().strip()
        try:
            attempts = int(self.attempts_entry.text())
            if not word:
                QMessageBox.critical(self, "Error", "La palabra no puede estar vacía.")
                return
            if attempts < 1:
                QMessageBox.critical(self, "Error", "Los intentos deben ser mayor a 0.")
                return
            
            self.controller.start_game(word, desc, attempts)
            self.show_game()
            
        except ValueError:
            QMessageBox.critical(self, "Error", "Intentos debe ser un número.")

    def guess_action(self, char):
        self.controller.guess_letter(char)

    def update_ui(self, masked_word, attempts, description, game_over=False):
        self.word_label.setText(masked_word)
        self.status_label.setText(f"Intentos restantes: {attempts}")
        self.info_label.setText(f"Pista: {description}")
        
        if game_over:
            for btn in self.letter_buttons.values():
                btn.setEnabled(False)
        
    def draw_hangman(self, attempts_left, max_attempts):
        self.canvas.update_state(attempts_left, max_attempts)

    def disable_button(self, char):
        if char in self.letter_buttons:
            self.letter_buttons[char].setEnabled(False)
            
    def reset_keyboard(self):
        for btn in self.letter_buttons.values():
            btn.setEnabled(True)
