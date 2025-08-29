# Introduction of PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        # self.setGeometry(x,y, width, height)

        # self.setGeometry(0, 0, 500, 500)

        # adding image

        self.setWindowIcon(QIcon("profile.jpg"))





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()