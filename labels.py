# Labels PyQt5
import sys
from tkinter.constants import HORIZONTAL

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

# used for alignment
from PyQt5.QtCore import Qt


# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")

        self.setGeometry(600, 250, 800, 600)

        # adding icon image

        self.setWindowIcon(QIcon("profile.png"))

        # labels are used to display text or images

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: #a1aef0;"
                            "font-weight: bold;"
                            "font-style:italic;"
                            "text-decoration: underline;")
        # label.setAlignment(Qt.AlignTop)   # VERTICAL TOP
        # label.setAlignment(Qt.AlignBottom)  # BOTTOM TOP
        # label.setAlignment(Qt.AlignLeft)    # LEFT TOP
        # label.setAlignment(Qt.AlignRight)   # RIGHT TOP

        # label.setAlignment(Qt.AlignVCenter)   # VERTICAL CENTER
        # label.setAlignment(Qt.AlignHCenter)   # HORIZONTAL CENTER
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop ) # ALIGN HORIZONTAL CENTER AND VERTICALLY TOP
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #ALIGN CENTER









def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()