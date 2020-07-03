import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from help1 import Ui_MainWindow


class frsttry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication()
    win = frsttry()
    sys.exit(app.exec_())
