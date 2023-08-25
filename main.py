from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import traceback
from random import randint
from sympy import isprime, mod_inverse, gcd
from PyQt5.QtCore import QThread
import time
from PyQt5.QtGui import QTextCharFormat, QColor

class WorkerThread(QThread):
    update_signal = pyqtSignal(list)
    update_line_edit = pyqtSignal(list)
    update_result = pyqtSignal(str)

    def __init__(self, data, Ca, Da, Cb, Db, p):
        super().__init__()
        self.data = data
        self.Ca = Ca
        self.Da = Da
        self.Cb = Cb
        self.Db = Db
        self.p = p
        self.is_running = True

    def stop(self):
        self.is_running = False

    def run(self):
        try:
            texter = ""
            for i in range (len(self.data)):
                if self.is_running == False:
                    return

                m = ord(self.data[i])
                x1 = pow(m, self.Ca, self.p)
                self.update_line_edit.emit(["1", x1])
                for i in range(101):
                    self.update_signal.emit(["1", i])
                    self.msleep(15)
                x2 = pow(x1, self.Cb, self.p)
                self.update_line_edit.emit(["2", x2])
                for i in range(101):
                    self.update_signal.emit(["2", i])
                    self.msleep(15)
                x3 = pow(x2, self.Da, self.p)
                self.update_line_edit.emit(["3", x3])
                for i in range(101):
                    self.update_signal.emit(["3", i])
                    self.msleep(15)
                x4 = pow(x3, self.Db, self.p)
                self.update_line_edit.emit(["4", x4])
                self.sleep(1)
                texter += chr(x4)
                self.update_result.emit(texter)
        except:
            traceback.print_exc()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 711)
        self.check = False
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 40, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.p_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.p_label.setObjectName("p_label")
        self.horizontalLayout.addWidget(self.p_label)
        self.p_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.p_lineEdit.setObjectName("p_lineEdit")
        self.horizontalLayout.addWidget(self.p_lineEdit)
        self.primal_label = QtWidgets.QLabel(self.centralwidget)
        self.primal_label.setGeometry(QtCore.QRect(340, 0, 231, 51))
        self.primal_label.setObjectName("primal_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(690, 160, 191, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.alice_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.alice_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.alice_label.setAlignment(QtCore.Qt.AlignCenter)
        self.alice_label.setObjectName("alice_label")
        self.verticalLayout_2.addWidget(self.alice_label)
        self.Ca_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Ca_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Ca_label.setObjectName("Ca_label")
        self.verticalLayout_2.addWidget(self.Ca_label)
        self.Ca_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Ca_lineEdit.setObjectName("Ca_lineEdit")
        self.verticalLayout_2.addWidget(self.Ca_lineEdit)
        self.Cb_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Cb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Cb_label.setObjectName("Cb_label")
        self.verticalLayout_2.addWidget(self.Cb_label)
        self.Da_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Da_lineEdit.setObjectName("Da_lineEdit")
        self.verticalLayout_2.addWidget(self.Da_lineEdit)
        self.A_generate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.A_generate_pushButton.setObjectName("A_generate_pushButton")
        self.verticalLayout_2.addWidget(self.A_generate_pushButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.rand_numb_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rand_numb_pushButton.setGeometry(QtCore.QRect(310, 100, 221, 28))
        self.rand_numb_pushButton.setObjectName("rand_numb_pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 160, 631, 161))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 140, 141, 16))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(690, 500, 191, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bob_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.bob_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.bob_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bob_label.setObjectName("bob_label")
        self.verticalLayout_4.addWidget(self.bob_label)
        self.Cb_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Cb_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Cb_label_3.setObjectName("Cb_label_3")
        self.verticalLayout_4.addWidget(self.Cb_label_3)
        self.Cb_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Cb_lineEdit.setObjectName("Cb_lineEdit")
        self.verticalLayout_4.addWidget(self.Cb_lineEdit)
        self.Cb_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Cb_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Cb_label_2.setObjectName("Cb_label_2")
        self.verticalLayout_4.addWidget(self.Cb_label_2)
        self.Db_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Db_lineEdit.setObjectName("Db_lineEdit")
        self.verticalLayout_4.addWidget(self.Db_lineEdit)
        self.B_generate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.B_generate_pushButton.setObjectName("B_generate_pushButton")
        self.verticalLayout_4.addWidget(self.B_generate_pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 500, 631, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 480, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 390, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 390, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 390, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 390, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 410, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 410, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(530, 410, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(750, 410, 141, 20))
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 450, 831, 26))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.X1_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.X1_lineEdit.setText("")
        self.X1_lineEdit.setReadOnly(True)
        self.X1_lineEdit.setObjectName("X1_lineEdit")
        self.horizontalLayout_2.addWidget(self.X1_lineEdit)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.X2_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.X2_lineEdit.setReadOnly(True)
        self.X2_lineEdit.setObjectName("X2_lineEdit")
        self.horizontalLayout_2.addWidget(self.X2_lineEdit)
        self.progressBar_2 = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_2.addWidget(self.progressBar_2)
        self.X3_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.X3_lineEdit.setReadOnly(True)
        self.X3_lineEdit.setObjectName("X3_lineEdit")
        self.horizontalLayout_2.addWidget(self.X3_lineEdit)
        self.progressBar_3 = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_2.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(11170, 11390, 55, 16))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.X4_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.X4_lineEdit.setReadOnly(True)
        self.X4_lineEdit.setObjectName("X4_lineEdit")
        self.horizontalLayout_2.addWidget(self.X4_lineEdit)
        self.send_message_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_pushButton.setGeometry(QtCore.QRect(120, 323, 180, 28))
        self.send_message_pushButton.setObjectName("send_message_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(310, 323, 181, 28))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.stop_pushButton.setText("Завершить демонстрацию")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(500, 330, 141, 16))
        self.label_11.setObjectName("label_11")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(650, 330, 81, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.rand_numb_pushButton.clicked.connect(self.generate_p)
        self.send_message_pushButton.clicked.connect(self.send_message)
        self.stop_pushButton.clicked.connect(self.stop_thread)
        self.A_generate_pushButton.clicked.connect(lambda: self.generate_numbers("A"))
        self.B_generate_pushButton.clicked.connect(lambda: self.generate_numbers("B"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def error_input(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка ввода")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def check_input(self, number):
        try:
            number = int(number)
            if number <= 1:
                return False
            return True
        except ValueError:
            return False

    def generate_numbers(self, param):
        try:
            if self.p_lineEdit.text() == "":
                self.error_input("Сначала введите P")
                return
            if self.check_input(self.p_lineEdit.text()) == False or isprime(int(self.p_lineEdit.text())) == False:
                self.error_input("p должно быть простым числом")
                return
            p = int(self.p_lineEdit.text())
            if p <= 2:
                self.error_input("p должно быть > 2")
                return
            c = randint(1, p - 1)
            while gcd(c, p-1) != 1:
                c = randint(1, p - 1)
            d = mod_inverse(c, p-1)
            if param == "A":
                self.Ca_lineEdit.setText(str(c))
                self.Da_lineEdit.setText(str(d))
            else:
                self.Cb_lineEdit.setText(str(c))
                self.Db_lineEdit.setText(str(d))
        except:
            traceback.print_exc()

    def generate_p(self):
        try:
            while True:
                p = randint(2000000, 9999999)
                if isprime(p):
                    self.p_lineEdit.setText(str(p))
                    return
        except:
            traceback.print_exc()

    def send_message(self):
        try:
            self.check = False
            self.textBrowser_2.setText("")
            if self.p_lineEdit.text() == "":
                self.error_input("Сначала введите P")
                return
            if self.check_input(self.p_lineEdit.text()) == False or isprime(int(self.p_lineEdit.text())) == False:
                self.error_input("p должно быть простым числом")
                return
            p = int(self.p_lineEdit.text())
            if p <= 3:
                self.error_input("p должно быть > 3")
                return

            if self.Ca_lineEdit.text() == "" or self.Da_lineEdit.text() == "" or \
                self.check_input(self.Ca_lineEdit.text()) == False or self.check_input(self.Da_lineEdit.text()) == False:
                self.error_input("Ca и Da должны быть натуральными")
                return

            if self.Cb_lineEdit.text() == "" or self.Db_lineEdit.text() == "" or \
                self.check_input(self.Cb_lineEdit.text()) == False or self.check_input(self.Db_lineEdit.text()) == False:
                self.error_input("Cb и Db должны быть натуральными")
                return

            Ca = int(self.Ca_lineEdit.text())
            Cb = int(self.Cb_lineEdit.text())
            Da = int(self.Da_lineEdit.text())
            Db = int(self.Db_lineEdit.text())

            if (Ca*Da) % (p-1) != 1:
                self.error_input("Ca * Da % (p-1) должно равняться 1")

            if (Cb*Db) % (p-1) != 1:
                self.error_input("Cb * Db % (p-1) должно равняться 1")

            text = self.textBrowser.toPlainText()
            texter = ""
            check = False
            if self.checkBox.checkState() == 2:
                check = True

            if check != True:
                for i in range(len(text)):
                    if ord(text[i]) >= p:
                        self.error_input("m должно быть меньше модуля p")
                        return
                    m = ord(text[i])
                    x1 = pow(m, Ca, p)
                    x2 = pow(x1, Cb, p)
                    x3 = pow(x2, Da, p)
                    x4 = pow(x3, Db, p)
                    texter += chr(x4)
                self.textBrowser_2.setText(texter)
            else:
                for i in range(len(text)):
                    if ord(text[i]) >= p:
                        self.error_input("m должно быть меньше модуля p")
                        return
                try:
                    self.worker_thread = WorkerThread(text, Ca, Da, Cb, Db, p)
                    self.worker_thread.update_signal.connect(self.progress_bar)
                    self.worker_thread.update_result.connect(self.output)
                    self.worker_thread.update_line_edit.connect(self.lines)
                    self.worker_thread.start()
                    self.check = True
                except:
                    traceback.print_exc()
        except:
            traceback.print_exc()

    def stop_thread(self):
        if self.checkBox.checkState() != 2 or self.check == False:
            self.error_input("Для начала надо ее запустить")
            return
        self.worker_thread.stop()
        self.check = False

    def output(self, texter):
        self.textBrowser_2.setText(texter)
        self.X1_lineEdit.setText("")
        self.X2_lineEdit.setText("")
        self.X3_lineEdit.setText("")
        self.X4_lineEdit.setText("")
        self.progressBar.setValue(int(0))
        self.progressBar_2.setValue(int(0))
        self.progressBar_3.setValue(int(0))

    def lines(self, params):
        if params[0] == "1":
            self.X1_lineEdit.setText(str(params[1]))
        if params[0] == "2":
            self.X2_lineEdit.setText(str(params[1]))
        if params[0] == "3":
            self.X3_lineEdit.setText(str(params[1]))
        if params[0] == "4":
            self.X4_lineEdit.setText(str(params[1]))

    def progress_bar(self, params):
        if params[0] == "1":
            self.progressBar.setValue(int(params[1]))
        if params[0] == "2":
            self.progressBar_2.setValue(int(params[1]))
        if params[0] == "3":
            self.progressBar_3.setValue(int(params[1]))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шамир"))
        self.p_label.setText(_translate("MainWindow", "p ="))
        self.primal_label.setText(_translate("MainWindow", "Введите простое числo"))
        self.alice_label.setText(_translate("MainWindow", "Алиса"))
        self.Ca_label.setText(_translate("MainWindow", "Выберите число Са"))
        self.Cb_label.setText(_translate("MainWindow", "Выберите число Da"))
        self.A_generate_pushButton.setText(_translate("MainWindow", "Сгенерировать числа"))
        self.rand_numb_pushButton.setText(_translate("MainWindow", "Сгенерировать случайное число"))
        self.label.setText(_translate("MainWindow", "Введите сообщение"))
        self.bob_label.setText(_translate("MainWindow", "Боб"))
        self.Cb_label_3.setText(_translate("MainWindow", "Выберите число Cb"))
        self.Cb_label_2.setText(_translate("MainWindow", "Выберите число Db"))
        self.B_generate_pushButton.setText(_translate("MainWindow", "Сгенерировать числа"))
        self.label_2.setText(_translate("MainWindow", "Полученное сообщение"))
        self.label_3.setText(_translate("MainWindow", "Алиса"))
        self.label_4.setText(_translate("MainWindow", "Алиса"))
        self.label_5.setText(_translate("MainWindow", "Боб"))
        self.label_6.setText(_translate("MainWindow", "Боб"))
        self.label_7.setText(_translate("MainWindow", "X1 = m^Ca % p"))
        self.label_8.setText(_translate("MainWindow", "X2 = X1^Cb % p"))
        self.label_9.setText(_translate("MainWindow", "X3 = X2^Da % p"))
        self.label_10.setText(_translate("MainWindow", "X4 = X3^Db % p = m"))
        self.send_message_pushButton.setText(_translate("MainWindow", "Передать сообщение"))
        self.label_11.setText(_translate("MainWindow", "Демонстрация работы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
