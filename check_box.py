# Check Boxes of PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QCheckBox)
from PyQt5.QtCore import Qt



# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")

        self.check_box = QCheckBox("Do you like Food", self)
        self.setGeometry(600, 250, 800, 600)
        self.initUI()



    def initUI(self):
         # pass
        self.check_box.setGeometry(0, 0, 400, 100)

        self.check_box.setStyleSheet("font-size: 30px;"
                           "font-family: Arial;")
        self.check_box.setChecked(False)
        self.check_box.stateChanged.connect(self.checkbox_changed)


    def checkbox_changed(self, state):
        # print("you like food")
        # print(state)

        # when check box is checked state takes value 2 else o
        # if state == 2:
            # or
        if state == Qt.Checked:
            print("you like food!")
        else:
            print("you DONT like food!")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())