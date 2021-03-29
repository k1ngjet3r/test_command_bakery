'''
    Steps for signing in the Google Account via Google Maps
    1. click maps icon
    2. Tap user icon on the top right conor
    3. Tap "sign in on the car screen
    4. Enter username
    5. Tap Next btn
    6. Enter password
    7. Tap Next btn
    8. Tap Done
'''
import json, time, os
from img_search import find_and_tap

img = 'img\\ui_icon\\'

def sign_in_google_account():
    with open('json\\google_account.json') as ac:
        account = json.load(ac)

    # tap google maps
    find_and_tap('google_maps_icon.png')

    # tap user icon
    find_and_tap('sign_out_user_icon.png')

    # tap sign in to google 
    find_and_tap('sign_in_to_google_text.png')
    time.sleep(5)

    # sing in on car screen
    find_and_tap('sign_in_on_car_screen.png')
    time.sleep(10)

    # tap username entry field and enter username
    find_and_tap('username_entry_field.png')
    os.system('adb shell input text "{}"'.format(account['username']))
    find_and_tap('next_btn.png')
    time.sleep(8)

    # tap password entry field and enter password
    find_and_tap('password_entry_field.png')
    os.system('adb shell input text "{}"'.format(account['password']))
    find_and_tap('next_btn.png')
    time.sleep(10)

    #tap done
    find_and_tap('done_btn.png')


def sign_out_google_account():
    # tap google maps
    find_and_tap('google_maps_icon.png')

    # tap user icon
    find_and_tap('sign_in_user_icon.png')

    # tap sign out google account
    find_and_tap('sign_out_btn.png')

# sign_in_google_account()