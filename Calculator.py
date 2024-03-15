from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet("font-size:  30px; background-color: #505008")

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("0")

        self.btn1 = QPushButton("C")
        self.btn1.setStyleSheet("background-color: #D2C6C3")
        self.btn2 = QPushButton("#")
        self.btn2.setStyleSheet("background-color: #000000")
        self.btn3 = QPushButton("%")
        self.btn3.setStyleSheet("background-color: #000000")
        self.btn4 = QPushButton("÷")
        self.btn4.setStyleSheet("background-color: #000000")
       
        self.vbox1 = QHBoxLayout()
        self.vbox1.addWidget(self.edit)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)
        self.vbox.addWidget(self.btn4)

        self.setLayout(self.vbox)
        self.setLayout(self.vbox1)

        self.show()

app = QApplication([])
win = Win()
app.exec()
