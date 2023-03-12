import os
from pyqadmin import admin 
import ctypes, sys

#sc config HPSysInfoCap start=auto

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #os.system("net stop HPSysInfoCap")
    a = int(input())
    if a == "1":
        os.system("net stop AppIDSvc") # Удостоверение приложения
        os.system("net stop NetTcpPortSharing") # Пример совместного использования портов Net.TCP
        os.system("net stop AJRouter") # Служба маршрутизатора AllJoyn
        os.system("net stop bthserv") # Служба поддержки Bluetooth(надо убрать)
        os.system("net stop BDESVC") # Служба шифрования дисков BitLocker
        os.system("net stop RemoteRegistry") # Удаленный реестр
        os.system("net stop SensorService") # Служба датчиков
        os.system("net stop XboxNetApiSvc") # Сетевая служба Xbox Live
        os.system("net stop WbioSrvc") # Биометрическая служба Windows
        os.system("net stop SensorDataService") # Служба данных датчиков
        os.system("net stop seclogon") # Вторичный вход в систему
        os.system("net stop DiagTrack") # Функциональные возможности для подключенных пользователей и телеметрия
        os.system("net stop Fax") # Факс

    elif a == "2":
        os.system("net start AppIDSvc") # Удостоверение приложения
        os.system("net start NetTcpPortSharing") # Пример совместного использования портов Net.TCP
        os.system("net start AJRouter") # Служба маршрутизатора AllJoyn
        os.system("net start bthserv") # Служба поддержки Bluetooth(надо убрать)
        os.system("net start BDESVC") # Служба шифрования дисков BitLocker
        os.system("net start RemoteRegistry") # Удаленный реестр
        os.system("net start SensorService") # Служба датчиков
        os.system("net start XboxNetApiSvc") # Сетевая служба Xbox Live
        os.system("net start WbioSrvc") # Биометрическая служба Windows
        os.system("net start SensorDataService") # Служба данных датчиков
        os.system("net start seclogon") # Вторичный вход в систему
        os.system("net start DiagTrack") # Функциональные возможности для подключенных пользователей и телеметрия
        os.system("net start Fax") # Факс

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
