import os
import time

'''
    This is mainly designed for 10" screen only
    There is currently no program for 13"
'''
def adb_root():
    os.system('adb root')

def online():
    os.system('adb shell "svc wifi enable"')


def offline():
    os.system('adb shell "svc wifi disable"')


def sign_in():
    adb_root()
    os.system('adb shell input tap 0 600')
    os.system('adb shell input tap 1850 200')
    os.system('adb shell input tap 700 500')
    time.sleep(6)
    os.system('adb shell input tap 700 700')
    time.sleep(6)
    os.system('adb shell input tap 700 550')
    time.sleep(3)
    os.system('adb shell input text "gm.testing.phone"')
    os.system('adb shell input tap 1850 200')
    time.sleep(6)
    os.system('adb shell input text "2019Go1101"')
    os.system('adb shell input tap 1850 200')
    time.sleep(6)
    os.system('adb shell input tap 1850 200')


def sign_out():
    adb_root()
    os.system('adb shell input tap 0 600')
    os.system('adb shell input tap 1850 200')
    os.system('adb shell input tap 600 700')

def pin_lock():
    adb_root()
    os.system('adb shell locksettings set-pin 0000')

def pw_lock():
    adb_root()
    os.system('adb shell locksettings set-password 0000')

def pattern_lock():
    adb_root()
    os.system('adb shell locksettings set-pattern 14789')
