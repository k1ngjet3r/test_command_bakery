import os

def play_pause():
    os.system('adb shell input keyevent 85')

def next_act():
    os.system('adb shell input keyevent 87')

def previous_act():
    os.system('adb shell input keyevent 88')