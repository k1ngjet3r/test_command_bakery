import pyttsx3, os, time

from pyttsx3 import engine


def activate_ga():
    os.system('adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity')

def tts(query):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    # giving the command via speaker
    engine.say(query)
    engine.runAndWait()

def hey_google_cmd(query):
    tts('Hey Google')
    time.sleep(1)
    tts(query)

def adb_cmd(query):
    activate_ga()
    time.sleep(2)
    tts(query)

# hey_google_cmd('Hello')
if __name__ == '__main__':
    frame = 'adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity -e query '
    frame = frame.split()
    frame.append('Majaja')
    print(frame)