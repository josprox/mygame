import sys
import os
from PySide6.QtWidgets import QApplication
from styles import WINUI_STYLESHEET

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.path)
    app.setStyleSheet(WINUI_STYLESHEET)
    
    controller = MainController()
    controller.run()
    
    sys.exit(app.exec())
