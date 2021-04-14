from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
import sys
from untitled import Ui_Form as wewe
__author__ = 'Abdullah Alaa'

class MainApp(QMainWindow, wewe):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    def Handel_UI(self):
        self.setFixedSize(291, 376)

    def Handel_Buttons(self):
        self.pushButton_16.clicked.connect(self.zero)
        self.pushButton_9.clicked.connect(self.n1)
        self.pushButton_8.clicked.connect(self.n2)
        self.pushButton_7.clicked.connect(self.n3)
        self.pushButton_4.clicked.connect(self.n4)
        self.pushButton_5.clicked.connect(self.n5)
        self.pushButton_6.clicked.connect(self.n6)
        self.pushButton_3.clicked.connect(self.n7)
        self.pushButton_2.clicked.connect(self.n8)
        self.pushButton_10.clicked.connect(self.n9)
        self.pushButton_11.clicked.connect(self.Pls)
        self.pushButton_13.clicked.connect(self.Plns)
        self.pushButton_17.clicked.connect(self.fee)
        self.pushButton_12.clicked.connect(self.tr7)
        self.pushButton.clicked.connect(self.ntega)
        self.pushButton_18.clicked.connect(self.clear)
        self.pushButton_19.clicked.connect(self.delete)
        self.pushButton_20.clicked.connect(self.ng)


    def zero(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"0")

    def n1(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"1")

    def n2(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"2")

    def n3(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"3")

    def n4(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"4")

    def n5(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"5")

    def n6(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"6")

    def n7(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"7")

    def n8(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"8")

    def ng(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A + ".")

    def n9(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"9")

    def Pls(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"+")

    def Plns(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"-")

    def fee(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"*")

    def tr7(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A+"/")

    def ntega(self):
        try:
            A = self.textEdit.toPlainText()
            B = eval(A)
            self.textEdit.setText(str(B))
        except:
            QMessageBox.warning(self,"Error","I cannot calculate this!")

    def clear(self):
        self.textEdit.setText('')

    def delete(self):
        A = self.textEdit.toPlainText()
        self.textEdit.setText(A[:-1])

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()