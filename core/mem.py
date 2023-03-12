import os
from pyqadmin import admin 
import ctypes, sys

#sc config HPSysInfoCap start=auto

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def nge():
    if is_admin():
        os.system("zxc.exe workingsets")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)   
