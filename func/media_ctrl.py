import os

def play_pause():
    os.system('adb shell input keyevent 85')

def next_act():
    os.system('adb shell input keyevent 87')

def previous_act():
    os.system('adb shell input keyevent 88')

def volume_up():
    os.system('adb shell input keyevent 24')

def volume_down():
    os.system('adb shell input keyevent 25')

def mute():
    os.system('adb shell input keyevent 164')
