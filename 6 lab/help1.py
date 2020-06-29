from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1495, 743)
        self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton("Поиск по логину", self.centralwidget)
        # self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 90, 161, 41))
        self.pushButton.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.pushButton_2 = QPushButton("Поиск по временному диапазону", self.centralwidget)
        # self.pushButton_2 = QPushButton(self.centralwidget)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 140, 301, 41))
        self.pushButton_2.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(self.centralwidget.resize(1495, 743))
        self.pushButton.clicked.connect(self.call())
        self.pushButton_2.clicked.connect(self.widget.hide())

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def call(self):
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(10, 190, 1481, 541))
        self.pushButton_4 = QPushButton("Загрузить csv файл", self.widget)
        self.pushButton_4.setGeometry(QRect(1260, 490, 181, 41))
        self.pushButton_4.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setGeometry(QRect(10, 10, 1031, 451))
        self.tableWidget_2 = QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QRect(1080, 80, 351, 381))
        self.label = QLabel("Доступные пользователи:", self.widget)
        self.label.setGeometry(QRect(1140, 30, 251, 41))
        self.label.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.widget.show()
    # def retranslateUi(self, MainWindow):
    #     MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    #     self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043b\u043e\u0433\u0438\u043d\u0443", None))
    #     self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u043c\u0443 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0443", None))
    #     self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c csv \u0444\u0430\u0439\u043b", None))
    #     self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438:</span></p></body></html>", None))
    # retranslateUi

