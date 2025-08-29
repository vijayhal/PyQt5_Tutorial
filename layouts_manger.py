# Layouts Manager of PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout)



# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        self.setGeometry(600, 250, 800, 600)
        self.initUI()



    def initUI(self):
        # pass

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:blue;")
        label3.setStyleSheet("background-color:orange;")
        label4.setStyleSheet("background-color:green;")
        label5.setStyleSheet("background-color:purple;")

        ##VERTICAL LAYOUT

        # vbox = QVBoxLayout()
        #
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        #
        # central_widget.setLayout(vbox)
        #

        # # HORIZONTAL LAYOUT
        #
        # hbox = QHBoxLayout()
        #
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        #
        # central_widget.setLayout(hbox)

        # GRID LAYOUT

        grid = QGridLayout()

        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,3,4)

        central_widget.setLayout(grid)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()