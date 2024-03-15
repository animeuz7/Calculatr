from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("🧮")
        self.setStyleSheet("background-color: #ccccff")
        
        self.edit = QLineEdit()

        self.btn1 = QPushButton("C")
        self.btn1.setStyleSheet("background-color: #D2C6C3")
        self.btn1.clicked.connect(self.clear_input)

        self.btn2 = QPushButton("ABC")
        self.btn2.setStyleSheet("background-color: #D2C6C3")
        # For future functionality

        self.btn3 = QPushButton("%")
        self.btn3.setStyleSheet("background-color: #D2C6C3")
        # For future functionality

        self.btn4 = QPushButton("/")
        self.btn4.setStyleSheet("background-color: #D2C6C3")
        self.btn4.clicked.connect(lambda: self.append_operator("/"))

        self.btn5 = QPushButton("7")
        self.btn5.clicked.connect(lambda: self.append_number("7"))

        self.btn6 = QPushButton("8")
        self.btn6.clicked.connect(lambda: self.append_number("8"))

        self.btn7 = QPushButton("9")
        self.btn7.clicked.connect(lambda: self.append_number("9"))

        self.btn8 = QPushButton("*")
        self.btn8.setStyleSheet("background-color: #D2C6C3")
        self.btn8.clicked.connect(lambda: self.append_operator("*"))

        self.btn9 = QPushButton("4")
        self.btn9.clicked.connect(lambda: self.aappend_numberdd("4"))

        self.btn10 = QPushButton("5")
        self.btn10.clicked.connect(lambda: self.append_number("5"))

        self.btn11 = QPushButton("6")
        self.btn11.clicked.connect(lambda: self.append_number("6"))

        self.btn12 = QPushButton("-")
        self.btn12.setStyleSheet("background-color: #D2C6C3")
        self.btn12.clicked.connect(lambda: self.append_operator("-"))

        self.btn13 = QPushButton("1")
        self.btn13.clicked.connect(lambda: self.aappend_numberdd("1"))

        self.btn14 = QPushButton("2")
        self.btn14.clicked.connect(lambda: self.append_number("2"))

        self.btn15 = QPushButton("3")
        self.btn15.clicked.connect(lambda: self.append_number("3"))

        self.btn16 = QPushButton("+")
        self.btn16.setStyleSheet("background-color: #D2C6C3")
        self.btn16.clicked.connect(lambda: self.append_operator("+"))

        self.btn17 = QPushButton("0")
        self.btn17.clicked.connect(lambda: self.append_number("0"))

        self.btn18 = QPushButton(".")
        self.btn18.clicked.connect(lambda: self.append_number("."))

        self.btn19 = QPushButton("<—")
        self.btn19.clicked.connect(self.remove_last_character)

        self.btn20 = QPushButton("=")
        self.btn20.setStyleSheet("background-color: #EDEA15")
        self.btn20.clicked.connect(self.calculate_result)

        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.hbox0.addWidget(self.edit)

        self.hbox1.addWidget(self.btn1)
        self.hbox1.addWidget(self.btn2)
        self.hbox1.addWidget(self.btn3)
        self.hbox1.addWidget(self.btn4)

        self.hbox2.addWidget(self.btn5)
        self.hbox2.addWidget(self.btn6)
        self.hbox2.addWidget(self.btn7)
        self.hbox2.addWidget(self.btn8)

        self.hbox3.addWidget(self.btn9)
        self.hbox3.addWidget(self.btn10)
        self.hbox3.addWidget(self.btn11)
        self.hbox3.addWidget(self.btn12)

        self.hbox4.addWidget(self.btn13)
        self.hbox4.addWidget(self.btn14)
        self.hbox4.addWidget(self.btn15)
        self.hbox4.addWidget(self.btn16)

        self.hbox5.addWidget(self.btn17)
        self.hbox5.addWidget(self.btn18)
        self.hbox5.addWidget(self.btn19)
        self.hbox5.addWidget(self.btn20)

        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)
        self.show()

        self.expression = ""

    def append_number(self, number):
        self.expression += number
        self.edit.setText(self.expression)

    def append_operator(self, operator):
        self.expression += operator
        self.edit.setText(self.expression)

    def clear_input(self):
        self.expression = ""
        self.edit.clear()

    def remove_last_character(self):
        self.expression = self.expression[:-1]
        self.edit.setText(self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.edit.setText(str(result))
        except Exception as e:
            self.edit.setText("Error")
            
    def append_operator(self, operator):
        if self.expression and self.expression[-1] in ['+', '-', '*', '/' '.' '0']:
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator
            self.edit.setText(self.expression)


app = QApplication([])
win = Win()
app.exec_()
