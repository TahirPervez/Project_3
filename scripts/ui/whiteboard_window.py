import sys
import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget, QHBoxLayout

class WhiteboardWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Develop a Recipe")
        self.setGeometry(150, 150, 300, 200)
        
        layout = QVBoxLayout()
        
        #Change to search from your ingredients
        self.suggest_button = QPushButton("Select Your Starting Point(s):", self)
        layout.addWidget(self.suggest_button)
        
        self.back_button = QPushButton("Back to Main Menu", self)
        self.back_button.clicked.connect(self.close_stove)
        layout.addWidget(self.back_button)
        
        self.setLayout(layout)
    
    def close_stove(self):
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = WhiteboardWindow(None)
    window.show()
    sys.exit(app.exec())