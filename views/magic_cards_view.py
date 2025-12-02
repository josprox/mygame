from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QFrame, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont

class MagicCardsView(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        
        self.intro_widget = QWidget()
        self.game_widget = QWidget()
        self.result_widget = QWidget()
        
        self.create_intro_ui()
        self.create_game_ui()
        self.create_result_ui()
        
        self.layout.addWidget(self.intro_widget)
        self.layout.addWidget(self.game_widget)
        self.layout.addWidget(self.result_widget)
        
        self.show_intro()

    def show_intro(self):
        self.game_widget.hide()
        self.result_widget.hide()
        self.intro_widget.show()

    def show_game(self):
        self.intro_widget.hide()
        self.result_widget.hide()
        self.game_widget.show()

    def show_result(self, number):
        self.intro_widget.hide()
        self.game_widget.hide()
        self.result_label.setText(f"¡Tu número es el {number}!")
        self.result_widget.show()

    def create_intro_ui(self):
        layout = QVBoxLayout(self.intro_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Cartas Mágicas")
        title.setProperty("class", "title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Piensa en un número del 1 al 31.")
        subtitle.setProperty("class", "subtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        btn_start = QPushButton("¡Estoy listo!")
        btn_start.setProperty("class", "accent")
        btn_start.clicked.connect(self.controller.start_game)
        layout.addWidget(btn_start)
        
        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(self.controller.go_back)
        layout.addWidget(btn_back)

    def create_game_ui(self):
        layout = QVBoxLayout(self.game_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        # Card Frame
        self.card_frame = QFrame()
        self.card_frame.setFixedSize(300, 400)
        self.card_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #ddd;
            }
        """)
        
        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 5)
        self.card_frame.setGraphicsEffect(shadow)
        
        card_layout = QVBoxLayout(self.card_frame)
        card_layout.setAlignment(Qt.AlignCenter)
        
        self.card_label = QLabel("Carta X")
        self.card_label.setStyleSheet("color: darkred; font-size: 24px; font-weight: bold; border: none;")
        self.card_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.card_label)
        
        self.numbers_label = QLabel("")
        self.numbers_label.setStyleSheet("color: black; font-family: 'Courier New'; font-size: 18px; border: none;")
        self.numbers_label.setAlignment(Qt.AlignCenter)
        self.numbers_label.setWordWrap(True)
        card_layout.addWidget(self.numbers_label)
        
        layout.addWidget(self.card_frame)
        
        layout.addWidget(QLabel("¿Está tu número en esta carta?"))
        
        btn_layout = QHBoxLayout()
        
        yes_btn = QPushButton("SÍ")
        yes_btn.setStyleSheet("background-color: #4CAF50; border: none;")
        yes_btn.clicked.connect(lambda: self.controller.answer(True))
        btn_layout.addWidget(yes_btn)
        
        no_btn = QPushButton("NO")
        no_btn.setStyleSheet("background-color: #F44336; border: none;")
        no_btn.clicked.connect(lambda: self.controller.answer(False))
        btn_layout.addWidget(no_btn)
        
        layout.addLayout(btn_layout)

    def create_result_ui(self):
        layout = QVBoxLayout(self.result_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        self.result_label = QLabel("")
        self.result_label.setProperty("class", "title")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
        btn_again = QPushButton("Jugar de nuevo")
        btn_again.setProperty("class", "accent")
        btn_again.clicked.connect(self.show_intro)
        layout.addWidget(btn_again)
        
        btn_back = QPushButton("Volver al Menú")
        btn_back.clicked.connect(self.controller.go_back)
        layout.addWidget(btn_back)

    def update_card(self, index, numbers):
        self.card_label.setText(f"CARTA {index + 1}")
        
        content = ""
        for i in range(0, len(numbers), 4):
            row = numbers[i:i+4]
            content += " ".join(f"{num:^4}" for num in row) + "\n"
        
        self.numbers_label.setText(content)
