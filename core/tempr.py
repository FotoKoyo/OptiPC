import os
import shutil

del_dir = r'C:\Windows\Temp'

def temprr():
   for f in os.listdir(del_dir):
        if os.path.isfile(r'C:\Windows\Temp\\'+f):
            os.remove(r'C:\Windows\Temp\\'+f)

        elif os.path.isdir(r'C:\Windows\Temp\\'+f):
            shutil.rmtree(r'C:\Windows\Temp\\'+f, ignore_errors=True)
