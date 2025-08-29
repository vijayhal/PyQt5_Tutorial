# PushButtons Manager of PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton)



# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        self.button = QPushButton("Click me", self)
        self.label1 = QLabel("Hello", self)
        self.setGeometry(600, 250, 800, 600)
        self.initUI()



    def initUI(self):
        # pass

        self.button.setGeometry(300,200,200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.button.clicked.connect(self.on_click)

        self.label1.setGeometry(310,300,200,100)
        self.label1.setStyleSheet("font-size:50px;")


    def on_click(self):
        print("Button Clicked")
        self.button.setText("clicked!")
        self.button.setDisabled(True)
        self.label1.setText("Great!")












if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())