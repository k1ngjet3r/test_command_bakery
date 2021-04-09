import os
import time
import subprocess
from datetime import datetime
'''
    This is mainly designed for 10" screen only
    There is currently no program for 13"
'''

def check_adb_status():
    print('[Startup] Checking adb connection')
    connection = subprocess.check_output(['adb', 'devices']).splitlines()
    if len(connection) <= 2:
        print('         Cannot estiblish connection')
        return False
    else:
        for i in connection:
            i = i.decode('ascii').split()
            if 'fail' in i:
                print('         Cannot estiblish connection')
                return False
            print('         Adb Connected')
            return True
    
def adb_root():
    os.system('adb root')

def online():
    print('Turn on wifi')
    os.system('adb shell "svc wifi enable"')

def offline():
    print('Trun off wifi')
    os.system('adb shell "svc wifi disable"')

def pin_lock():
    print('Set PIN')
    adb_root()
    os.system('adb shell locksettings set-pin 0000')

def pw_lock():
    print('Set password')
    adb_root()
    os.system('adb shell locksettings set-password 0000')

def pattern_lock():
    # default is a L shape pattern
    print('Set pattern')
    adb_root()
    os.system('adb shell locksettings set-pattern 14789')

def screenshot():
    print('Getting the screenshot')
    path = os.getcwd().replace('\\', '/')+'/screenshot'
    now = datetime.now()
    name = '{}_{}_{}_{}'.format(now.day, now.hour, now.minute, now.second)
    os.system('adb shell screencap -p /sdcard/{}.png'.format(name))
    os.system('adb pull /sdcard/{}.png {}'.format(name, path))
    os.system('adb shell rm /sdcard/{}.png'.format(name))

def easter_egg():
    os.system('adb shell am broadcast -a android.intent.action.EASTEREGG --ez enable true')


if __name__ == '__main__':
    print(subprocess.check_output(['adb', 'devices']).splitlines())
    