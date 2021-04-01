# Majaja
## What is Majaja?
An Android-based devices testing aid, which has an ugly GUI and functions such as:
* Wifi control (online/offline)
* Google account sign-in or sign-out
* Create device's user
* Set PIN, password, or pattern locks
* Control music playback
* Give Google Assistant command
And it also has a space for meme because why not?

## Environment Requirment
1. Python 3.6+
2. Pillow module (pip install pillow)
3. OpenCV module (pip install opencv-python)
4. Playsound module (pip install playsound)

## How Majaja Work?
Most of the functions were directly controlled by sending adb command, however, since we cannot find the direct control for login or out of the google account, adb was used for simulate the tap to login or out the Google account

## First Time?
If this is your first time using Majaja, there are few things that you need to do:
1. Go to \json folder and create "google_account.json" to store google account's username and password
2. Create a folder named "temp" in the \img folder


