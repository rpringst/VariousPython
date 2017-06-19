import shutil
import threading


def printit():
    usage = shutil.disk_usage('/media/robert/C60C3AF90C3AE3D9/')
    oldval = usage[2]/(1024*1024*1024)
    threading.Timer(5.0, printit).start()
    usage = shutil.disk_usage('/media/robert/C60C3AF90C3AE3D9/')
    newval = usage[2]/(1024*1024*1024)
    print(str(newval-oldval))
    oldval = newval

printit()
