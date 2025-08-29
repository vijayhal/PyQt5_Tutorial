# Images PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
# QPixmap used for manipulation of images

# Boiler Plate Code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Fist GUI learning")
        self.setWindowIcon(QIcon("profile.jpg"))
        self.setGeometry(600, 250, 800, 600)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("profile.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        # Positioning of label

        label.setGeometry((self.width()-label.width()) // 2,
                            (self.height() - label.height()) // 2, label.width(), label.height())










def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()