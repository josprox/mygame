import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.main_controller import MainController

if __name__ == "__main__":
    app = MainController()
    app.run()
