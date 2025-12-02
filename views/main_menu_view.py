from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class MainMenuView(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)
        
        # Title
        title = QLabel("Colección de Juegos Python")
        title.setProperty("class", "title") # For CSS styling
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Selecciona un juego para comenzar")
        subtitle.setProperty("class", "subtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        # Buttons Container
        btn_container = QWidget()
        btn_layout = QVBoxLayout(btn_container)
        btn_layout.setSpacing(10)
        
        btn_hangman = QPushButton("El Ahorcado")
        btn_hangman.setCursor(Qt.PointingHandCursor)
        btn_hangman.setMinimumHeight(40)
        btn_hangman.clicked.connect(lambda: controller.show_game("hangman"))
        btn_layout.addWidget(btn_hangman)
        
        btn_magic = QPushButton("Cartas Mágicas")
        btn_magic.setCursor(Qt.PointingHandCursor)
        btn_magic.setMinimumHeight(40)
        btn_magic.clicked.connect(lambda: controller.show_game("magic_cards"))
        btn_layout.addWidget(btn_magic)
        
        btn_river = QPushButton("El Río")
        btn_river.setCursor(Qt.PointingHandCursor)
        btn_river.setMinimumHeight(40)
        btn_river.clicked.connect(lambda: controller.show_game("river"))
        btn_layout.addWidget(btn_river)
        
        layout.addWidget(btn_container)
        
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        
        btn_exit = QPushButton("Salir")
        btn_exit.setCursor(Qt.PointingHandCursor)
        btn_exit.setProperty("class", "accent") # Example of accent style if desired, or maybe keep it neutral
        btn_exit.clicked.connect(parent.close)
        layout.addWidget(btn_exit)
