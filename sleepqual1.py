import sys
import os
from sleepqual import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.intakefactrs)
     self.ui.pushButton_2.clicked.connect(self.rf)
     self.ui.pushButton_3.clicked.connect(self.gpc)
     self.ui.pushButton_4.clicked.connect(self.dplot)
     self.ui.pushButton_5.clicked.connect(self.strfactrs)

      

  def intakefactrs(self):
    os.system("python intake1.py")

  def rf(self):
    os.system("python -W ignore rforest1.py")

  def gpc(self):
    os.system("python gpc1.py")

  def dplot(self):
    os.system("python plot1.py")

  def strfactrs(self):  
    os.system("python stress1.py")

       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
