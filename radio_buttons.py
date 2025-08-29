# Radio Buttons in PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup




# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        self.setGeometry(600, 250, 800, 600)

        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("Gift Card", self)

        self.radio4 = QRadioButton("In Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()



    def initUI(self):
         # pass
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)

        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # self.radio1.setStyleSheet("font-size: 30px;"
        #                    "font-family: Arial;")

        # RATHER THAN APPLYING STYLESHEET TO EACH BUTTIONS WE CAN APPLY TO THE WIDGETS

        self.setStyleSheet("QRadioButton{"
                           "font-size:40px;"
                           "font-family:Arial;"
                           "padding:10px;}")

        # ADDING RADIO BUTTONS GROUP WISE

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)






    def radio_button_changed(self):
        # pass
        # print("you selected something")

        radio_button = self.sender()

        if radio_button.isChecked():
            print(f" Selected {radio_button.text()}")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())