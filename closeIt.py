import win32gui
import os
import ctypes
import sys
os.system("pip install psutil >nul")
import psutil

try:
    a = open("C:\\pid.txt")
except:
    exit()

pid1 = int(a.readlines()[0].replace("\n", ""))
if pid1 == 99999999:
    exit()
for pid in psutil.pids():
    if pid == pid1:
        print("check suscess")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit()

print("Noprocess!")

#创建pid。txt os.getpid(), 运行, 停止就输9999999
