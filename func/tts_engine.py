import pyttsx3, os, time

from pyttsx3 import engine


def activate_ga():
    os.system('adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity')

def tts(query):
    engine = pyttsx3.init()
    engine.setProperty('rate', 105)
    # giving the command via speaker
    engine.say(query)
    engine.runAndWait()

def hey_google_cmd(query):
    tts('Hey Google')
    time.sleep(0.8)
    tts(query)

def adb_cmd(query):
    activate_ga()
    time.sleep(0.8)
    tts(query)

# hey_google_cmd('Hello')