import sys
import time
import csv
import os
from inspect import getsourcefile
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide2.QtGui import QFont
from help1 import Ui_MainWindow


# class Logi(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_UI()

#     def init_UI(self):
#         self.logb()
#         self.timeb()
#         self.setGeometry(750, 350, 500, 500)
#         self.show()
    
#     def logb(self):
#         logb = QPushButton("Поиск по логину", self)
#         logb.setFont(QFont("Times New Roman", 14))
#         logb.resize(logb.sizeHint())
#         logb.move(155, 100)
    
#     def timeb(self):
#         timeb = QPushButton("Поиск по диапазону времени", self)
#         timeb.setFont(QFont("Times New Roman", 14))
#         timeb.resize(timeb.sizeHint())
#         timeb.move(100, 150)

#     def logsearch(self):
#         if os.path.exists("\\logs"):
#             os.chdir("logs")
#             for log in os.listdir("."):
#                 if log[-4] == ".csv":
#                     with open(log, "r") as f:
#                         red = csv.reader(f)
                        
#         else:
#             os.mkdir("logs")
#             print('Переместите ваши логи в папку "logs"')


class frsttry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
         


if __name__ == "__main__":
    # name = getsourcefile(lambda: 0)
    # if name is not None:
    #     os.chdir(os.path.dirname(os.path.abspath(name)))
    app = QApplication()
    # l = Logi()
    win = frsttry()
    sys.exit(app.exec_())
