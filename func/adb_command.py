import os
import time
import subprocess

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


# def sign_in():
#     adb_root()
#     os.system('adb shell input tap 0 600')
#     os.system('adb shell input tap 1850 200')
#     os.system('adb shell input tap 700 500')
#     time.sleep(6)
#     os.system('adb shell input tap 700 700')
#     time.sleep(6)
#     os.system('adb shell input tap 700 550')
#     time.sleep(3)
#     os.system('adb shell input text "gm.testing.phone"')
#     os.system('adb shell input tap 1850 200')
#     time.sleep(6)
#     os.system('adb shell input text "2019Go1101"')
#     os.system('adb shell input tap 1850 200')
#     time.sleep(6)
#     os.system('adb shell input tap 1850 200')


# def sign_out():
#     adb_root()
#     os.system('adb shell input tap 0 600')
#     os.system('adb shell input tap 1850 200')
#     os.system('adb shell input tap 600 700')

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
