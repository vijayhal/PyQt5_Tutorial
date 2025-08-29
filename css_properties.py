# CSS in PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout




# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")


        self.initUI()



    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        # instead of applying styles for buttons and labels , we will aplly for the window

        # creating objects of each button to apply the css property

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")





        self.setStyleSheet("""
        QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
        }
        QPushButton#button1{
                
                background-color: hsl(352, 80%, 65%);
        }
        
        QPushButton#button2{
                background-color: hsl(100, 100%, 80%);
        }
        
        QPushButton#button3{
                background-color: blue;
        }
        
        
        QPushButton#button2:hover{
                background-color: hsl(100, 100%, 40%);
        }
                
                
                
                
                
                
                
        """)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())