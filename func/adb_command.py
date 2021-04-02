import os
import time
import subprocess
from datetime import datetime
'''
    This is mainly designed for 10" screen only
    There is currently no program for 13"
'''

def check_adb_status():
    print('[DEBUG] Checking adb connection')
    connection = subprocess.check_output(['adb', 'devices']).splitlines()
    if len(connection) <= 1:
        return False
    else:
        for i in connection:
            i = i.decode('ascii').split()
            if 'fail' in i:
                return False
            return True
    
def adb_root():
    os.system('adb root')

def online():
    print('[DEBUG] turn on wifi')
    os.system('adb shell "svc wifi enable"')

def offline():
    print('[DEBUG] trun off wifi')
    os.system('adb shell "svc wifi disable"')

def pin_lock():
    print('[DEBUG] set PIN')
    adb_root()
    os.system('adb shell locksettings set-pin 0000')

def pw_lock():
    print('[DEBUG] set password')
    adb_root()
    os.system('adb shell locksettings set-password 0000')

def pattern_lock():
    # default is a L shape pattern
    print('[DEBUG] set pattern')
    adb_root()
    os.system('adb shell locksettings set-pattern 14789')

def screenshot():
    print('getting the screenshot')
    path = os.getcwd().replace('\\', '/')+'/screenshot'
    now = datetime.now()
    name = '{}_{}_{}_{}'.format(now.day, now.hour, now.minute, now.second)
    os.system('adb shell screencap -p /sdcard/{}.png'.format(name))
    os.system('adb pull /sdcard/{}.png {}'.format(name, path))
    os.system('adb shell rm /sdcard/{}.png'.format(name))
