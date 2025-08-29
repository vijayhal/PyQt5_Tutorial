# Line Edits in PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton




# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        self.setGeometry(600, 250, 800, 600)

        self.line_edit = QLineEdit(self)

        self.button1 = QPushButton(self)


        self.initUI()



    def initUI(self):
         self.line_edit.setGeometry(10,10, 200, 40)
         self.line_edit.setStyleSheet("font-size:20px;"
                                      "font-family:Arial;")

         self.line_edit.setPlaceholderText("Enter Your Name")

         self.button1.setGeometry(220, 10, 100, 40)
         self.button1.setStyleSheet("font-size:25px;"
                                 "font-family:Arial;")
         self.button1.setText("Submit")

         self.button1.clicked.connect(self.submit)

    def submit(self):
        # print("you clicked the button")

        input_text = self.line_edit.text()
        print(f"Hello {input_text}")










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())