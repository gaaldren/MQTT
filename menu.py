import sys 
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pub_an import Dialog
from sub_an import Dialog_sub

from ui_publisher import Ui_pub_form 
from ui_subscriber import Ui_sub_form
from ui_main import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sub_button.clicked.connect(self.openSub)
        self.ui.pub_button.clicked.connect(self.openPub)

    def openSub(self):
        dialog = Dialog_sub(self)
        self.hide()
        dialog.exec_()
    
    def openPub(self):   
        dialog = Dialog(self)
        self.hide()
        dialog.exec_()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())