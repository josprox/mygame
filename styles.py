# WinUI 3 inspired Dark Theme

WINUI_STYLESHEET = """
QWidget {
    background-color: #202020;
    color: #ffffff;
    font-family: "Segoe UI", "Helvetica", sans-serif;
    font-size: 14px;
}

/* Buttons */
QPushButton {
    background-color: #323232;
    border: 1px solid #3e3e3e;
    border-radius: 4px;
    padding: 8px 16px;
    color: #ffffff;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #3e3e3e;
    border: 1px solid #454545;
}

QPushButton:pressed {
    background-color: #292929;
    color: #cccccc;
}

QPushButton:disabled {
    background-color: #2b2b2b;
    color: #555555;
    border: 1px solid #2b2b2b;
}

/* Accent Button (Custom class) */
QPushButton[class="accent"] {
    background-color: #005FB8; /* Windows Blue */
    border: 1px solid #005FB8;
}

QPushButton[class="accent"]:hover {
    background-color: #1975D1;
    border: 1px solid #1975D1;
}

QPushButton[class="accent"]:pressed {
    background-color: #004C94;
}

/* Labels */
QLabel {
    color: #ffffff;
}

QLabel[class="title"] {
    font-size: 24px;
    font-weight: bold;
    color: #ffffff;
}

QLabel[class="subtitle"] {
    font-size: 18px;
    color: #cccccc;
}

/* Inputs */
QLineEdit {
    background-color: #2b2b2b;
    border: 1px solid #3e3e3e;
    border-radius: 4px;
    padding: 6px;
    color: #ffffff;
    selection-background-color: #005FB8;
}

QLineEdit:focus {
    border: 2px solid #005FB8; /* Focus border */
    background-color: #202020;
}

/* ListBox / QListWidget */
QListWidget {
    background-color: #2b2b2b;
    border: 1px solid #3e3e3e;
    border-radius: 4px;
    outline: none;
}

QListWidget::item {
    padding: 8px;
    border-radius: 4px;
    margin: 2px;
}

QListWidget::item:selected {
    background-color: #3e3e3e;
    color: #ffffff;
}

QListWidget::item:hover {
    background-color: #323232;
}

/* GroupBox */
QGroupBox {
    border: 1px solid #3e3e3e;
    border-radius: 6px;
    margin-top: 20px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 5px;
    color: #cccccc;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #202020;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #454545;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""
