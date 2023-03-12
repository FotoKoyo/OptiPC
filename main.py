import sys
from PyQt6.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_MainWindow
import os
import ctypes, sys
#from core.mem   import *
from core.tempr import *


def nge():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        os.system("zxc.exe workingsets")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.pushButton_4.clicked.connect(nge)
ui.pushButton_5.clicked.connect(temprr)
#ui.pushButton_6.clicked.connect(temprr)

window.show()
sys.exit(app.exec())
