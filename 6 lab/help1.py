import os
import csv
import datetime as dt
import time
import threading as tr
from inspect import getsourcefile
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Signal, QThread, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        if not self.MainWindow.objectName():
            self.MainWindow.setObjectName(u"MainWindow")
        self.MainWindow.setFixedSize(465, 245)
        self.centralwidget = QWidget(MainWindow)
        self.pushButton = QPushButton("Поиск по логину", self.centralwidget)
        self.pushButton.setGeometry(QRect(150, 90, 161, 41))
        self.pushButton.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.pushButton_2 = QPushButton("Поиск по дате", self.centralwidget)
        self.pushButton_2.setGeometry(QRect(150, 140, 161, 41))
        self.pushButton_2.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(10, 190, 1481, 541))
        self.pushButton_4 = QPushButton("Открыть папку с логами", self.widget)
        self.pushButton_4.setGeometry(QRect(1210, 490, 221, 41))
        self.pushButton_4.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.tableWidget = QTableWidget(0, 24, self.widget)
        self.tableWidget.setGeometry(QRect(10, 10, 1031, 451))
        self.tableWidget_2 = QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QRect(1080, 80, 351, 381))
        self.label = QLabel("Доступные пользователи:", self.widget)
        self.label.setGeometry(QRect(1140, 30, 251, 41))
        self.label.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.label_2 = QLabel("Введите дату(dd.mm.yyyy hh:mm):", self.widget)
        self.label_2.setGeometry(QRect(1100, 20, 331, 41))
        self.label_2.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.pushButton_5 = QPushButton("Сохранить результат", self.widget)
        self.pushButton_5.setGeometry(QRect(990, 490, 191, 41))
        self.pushButton_5.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QRect(940, 130, 111, 51))
        self.spinBox.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.label_3 = QLabel("Текущая страница таблицы", self.centralwidget)
        self.label_3.setGeometry(QRect(660, 130, 271, 41))
        self.label_3.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QRect(1160, 260, 211, 31))
        self.dateTimeEdit.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.pushButton_6 = QPushButton("Подтвердить", self.widget)
        self.pushButton_6.setGeometry(QRect(1190, 120, 151, 41))
        self.pushButton_6.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.label.close()
        self.label_2.close()
        self.label_3.close()
        self.tableWidget_2.close()
        self.pushButton_5.close()
        self.pushButton_6.close()
        self.spinBox.close()
        self.dateTimeEdit.close()
        self.widget.hide()
        self.xl = 0

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.lcall)
        self.pushButton_2.clicked.connect(self.tcall)
        self.pushButton_4.clicked.connect(self.loading)
        self.pushButton_5.clicked.connect(self.saving)
        self.spinBox.valueChanged.connect(self.filltable)
        self.pushButton_6.clicked.connect(self.confirm)

        QMetaObject.connectSlotsByName(MainWindow)

    def confirm(self) -> None:
        self.pushButton_5.show()
        self.tableWidget_2.clear()
        dtm = self.dateTimeEdit.dateTime()
        dtstr = dtm.toString(self.dateTimeEdit.displayFormat())
        x1 = dtstr + ':00'
        x2 = dtstr + ':59'
        x11 = dt.datetime.strptime(x1, '%d.%m.%Y %H:%M:%S')
        x22 = dt.datetime.strptime(x2, '%d.%m.%Y %H:%M:%S')
        begn = int(x11.timestamp())
        end = int(x22.timestamp())
        self.gettimses(begn, end)

    def lcall(self) -> None:
        if self.xl == 0:
            self.MainWindow.setFixedSize(1495, 743)
            self.MainWindow.move(self.MainWindow.x() - 515, self.MainWindow.y() - 249)
            self.xl = 1
        self.widget.show()
        self.label.show()
        self.tableWidget_2.show()
        self.label_2.close()
        self.dateTimeEdit.close()
        self.pushButton_6.close()

    def tcall(self) -> None:
        if self.xl == 0:
            self.MainWindow.setFixedSize(1495, 743)
            self.MainWindow.move(self.MainWindow.x() - 515, self.MainWindow.y() - 249)
            self.xl = 1
        self.widget.show()
        self.label_2.show()
        self.dateTimeEdit.show()
        self.label.close()
        self.tableWidget_2.close()

    def loading(self) -> None:
        lfile = QFileDialog(self)
        dirw = lfile.getExistingDirectory(self)
        name = getsourcefile(lambda: 0)
        if name is not None:
            self.orway = os.path.dirname(os.path.abspath(name))
            os.chdir(self.orway)
        if dirw != "":
            self.pushButton_5.close()
            os.chdir(dirw)
            global mode
            if self.dateTimeEdit.isHidden():
                mode = 1
            else:
                mode = 0
            self.perprogress()

    def loadingend(self, val: int) -> None:
        if val == 1:
            self.alssn = self.oralssn.copy()
            os.chdir(self.orway)
            lim = len(self.alssn[1:])
            mpt = 100
            self.fraglist = [mpt + mp * mpt + 1 for mp in range(lim//mpt)]
            if self.fraglist[-1] != lim:
                self.fraglist.append(len(self.alssn))
            if self.tableWidget_2.isHidden():
                self.pushButton_6.show()
            self.spinBox.show()
            self.spinBox.setRange(1, len(self.fraglist))
            if self.dateTimeEdit.isHidden():
                self.label_3.show()
                logl = set(self.logl)
                logl = list(logl)
                self.tableWidget_2.setRowCount(len(logl))
                self.tableWidget_2.setColumnCount(1)
                self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.tableWidget_2.setColumnWidth(0, 250)
                for logi, log in enumerate(logl):
                    cell = QTableWidgetItem()
                    cell.setData(Qt.DisplayRole, log)
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.tableWidget_2.setItem(logi - 1, 1, cell)
                self.tableWidget_2.cellPressed[int, int].connect(self.getses)
            self.filltable()

    def gettimses(self, begn: int, end: int) -> None:
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.alssn[0])
        self.tableWidget.setRowCount(0)
        curalssn = [self.oralssn[0]]
        for ses in self.oralssn[1:]:
            if int(ses[0]) >= begn and int(ses[0]) <= end:
                curalssn.append(ses)
        self.alssn.clear()
        self.alssn = curalssn
        lim = len(self.alssn[1:])
        mpt = 100
        self.fraglist = [mpt + mp * mpt + 1 for mp in range(lim//mpt)]
        try:
            if self.fraglist[-1] != lim:
                self.fraglist.append(len(self.alssn))
        except IndexError:
            self.fraglist = [len(self.alssn)]
        self.spinBox.setRange(1, len(self.fraglist))
        self.filltable()

    def getses(self) -> None:
        self.pushButton_5.show()
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.alssn[0])
        self.tableWidget.setRowCount(0)
        curalssn = [self.oralssn[0]]
        for ses in self.oralssn[1:]:
            if self.tableWidget_2.currentItem().data(Qt.DisplayRole) in ses:
                curalssn.append(ses)
        self.alssn.clear()
        self.alssn = curalssn
        lim = len(self.alssn[1:])
        mpt = 100
        self.fraglist = [mpt + mp * mpt + 1 for mp in range(lim//mpt)]
        try:
            if self.fraglist[-1] != lim:
                self.fraglist.append(len(self.alssn))
        except IndexError:
            self.fraglist = [len(self.alssn)]
        self.spinBox.setRange(1, len(self.fraglist))
        self.filltable()

    def saving(self) -> None:
        slist = [self.alssn[0]]
        for page in range(len(self.fraglist)):
            self.spinBox.setValue(page + 1)
            for i in range(self.tableWidget.rowCount()):
                rowl = [self.tableWidget.item(i, j).data(Qt.DisplayRole) for j in range(self.tableWidget.columnCount())]
                slist.append(rowl)
        lfile = QFileDialog(self)
        dirw = lfile.getSaveFileName(self, filter="Файл Microsoft Excel (*.csv)")
        if dirw != "":
            with open(dirw[0], "w", newline="") as fcsv:
                writer = csv.writer(fcsv)
                for row in slist:
                    writer.writerow(row)
                fcsv.seek(0, os.SEEK_END)
                fcsv.seek(fcsv.tell() - 2, os.SEEK_SET)
                fcsv.truncate()

    def filltable(self) -> None:
        self.tableWidget.clear()
        val = self.spinBox.value() - 1
        self.tableWidget.setHorizontalHeaderLabels(self.alssn[0])
        if val == 0:
            self.tableWidget.setRowCount(0)
            for rowi, row in enumerate(self.alssn[1:self.fraglist[0]]):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                for celli, cell in enumerate(row):
                    item = QTableWidgetItem()
                    item.setData(Qt.DisplayRole, cell)
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.tableWidget.setItem(rowi, celli, item)
        else:
            self.tableWidget.setRowCount(0)
            for rowi, row in enumerate(self.alssn[self.fraglist[val - 1]:self.fraglist[val]]):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                for celli, cell in enumerate(row):
                    item = QTableWidgetItem()
                    item.setData(Qt.DisplayRole, cell)
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.tableWidget.setItem(rowi, celli, item)

    def perprogress(self) -> None:
        self.Dialog = QDialog(self)
        self.Dialog.setFixedSize(380, 212)
        self.progressBar_2 = QProgressBar(self.Dialog)
        self.progressBar_2.setGeometry(QRect(170, 70, 181, 16))
        self.progressBar_2.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setAlignment(Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        self.progressBar_3 = QProgressBar(self.Dialog)
        self.progressBar_3.setGeometry(QRect(170, 150, 181, 16))
        self.progressBar_3.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.progressBar_3.setMinimum(0)
        self.progressBar_3.setMaximum(100)
        self.progressBar_3.setAlignment(Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_4 = QLabel(f"Текущий файл:\n", self.Dialog)
        self.label_4.setGeometry(QRect(20, 50, 141, 41))
        self.label_4.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.label_5 = QLabel(f"Текущая строка:\n", self.Dialog)
        self.label_5.setGeometry(QRect(20, 120, 141, 51))
        self.label_5.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.Dialog.setWindowModality(Qt.ApplicationModal)
        self.Dialog.show()
        self.startProgressBar()

    def startProgressBar(self) -> None:
        self.thread = loadThread()
        self.thread.countChanged1.connect(self.prlch)
        self.thread.countChanged2.connect(self.setProgressVal)
        self.thread.countChanged3.connect(self.prrch)
        self.thread.countChanged4.connect(self.setProgressVal2)
        self.thread.countChanged5.connect(self.setlist)
        self.thread.exits.connect(self.Dialog.deleteLater)
        self.thread.exits.connect(self.loadingend)
        self.thread.warning.connect(self.warning)
        self.thread.start()

    def prlch(self, val: str) -> None:
        self.label_4.setText(f"Текущий файл:\n{val}")

    def setProgressVal(self, val: int) -> None:
        self.progressBar_2.setValue(val)

    def prrch(self, val: str) -> None:
        self.label_5.setText(f"Текущая строка:\n{val}")

    def setProgressVal2(self, val: int) -> None:
        self.progressBar_3.setValue(val)

    def setlist(self, val: list) -> None:
        del self.thread
        global mode
        self.oralssn = val[0]
        if mode == 1:
            self.logl = val[1]

    def warning(self, val: str) -> None:
        self.warnDiag = QDialog(self)
        self.warnDiag.resize(310, 138)
        self.label = QLabel(f"Неверный формат записи\nфайла:{val}", self.warnDiag)
        self.label.setGeometry(QRect(30, 20, 251, 81))
        self.label.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.warnDiag.show()
        time.sleep(1.5)
        self.warnDiag.deleteLater()


class loadThread(QThread):
    countChanged1 = Signal(str)
    countChanged2 = Signal(int)
    countChanged3 = Signal(int)
    countChanged4 = Signal(int)
    countChanged5 = Signal(list)
    exits = Signal(int)
    warning = Signal(int)

    def run(self):
        oralssn = []
        logl = []
        maxf = len(os.listdir("."))
        global mode
        curl = 0
        ck = 0
        currow = 0
        corfiles = 0
        for log in os.listdir("."):
            self.countChanged1.emit(log)
            curl += 100 / maxf
            self.countChanged2.emit(curl)
            if log[-4:] == ".csv":
                curr = 0
                maxr = pd.read_csv(log, sep=",").shape[0]
                with open(log, "r") as f:
                    red = csv.reader(f)
                    lred = list(red)
                    del red
                    if len(lred[0]) != 24:
                        self.warning.emit(log)
                        continue
                    corfiles += 1
                    if ck == 0:
                        oralssn.append(lred[0])
                        ck = 1
                    for row in lred[1:]:
                        currow += 1
                        self.countChanged3.emit(currow)
                        curr += 100 / maxr
                        self.countChanged4.emit(curr)
                        oralssn.append(row)
                if mode == 1:
                    with open(log, "r") as f:
                        r = csv.DictReader(f)
                        for lg in r:
                            logl.append(lg["login"])
        if mode == 1:
            self.countChanged5.emit([oralssn, logl])
        else:
            self.countChanged5.emit([oralssn])
        if corfiles == 0:
            self.exits.emit(0)
        else:
            self.exits.emit(1)
