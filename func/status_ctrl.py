import json, time, os
from func.img_search import find_and_tap, checking_info_screen

img = 'img\\ui_icon\\'


def sign_in_google_account():

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

    with open('json\\google_account.json') as ac:
        account = json.load(ac)

    # tap google maps
    print('tap google maps')
    if not find_and_tap('google_maps_icon.png'):
        return

    # tap user icon
    print('tap user icon')
    if not find_and_tap('sign_out_user_icon.png'):
        return
    
    checking_info_screen()

    # tap sign in to google 
    print('tap sign in')
    if not find_and_tap('sign_in_to_google_text.png'):
        return
    
    checking_info_screen()

    # sing in on car screen
    print('tap sign in on car screen')
    if not find_and_tap('sign_in_on_car_screen.png'):
        return

    checking_info_screen()

    # tap username entry field and enter username
    print('tap username entry fielf and enter username')
    if not find_and_tap('username_entry_field.png'):
        return
    else:
        os.system('adb shell input text "{}"'.format(account['username']))
        if not find_and_tap('next_btn.png'):
            return
    
    checking_info_screen()

    # tap password entry field and enter password
    print('tap password entry field and enter password')
    if not find_and_tap('password_entry_field.png'):
        return
    else:
        os.system('adb shell input text "{}"'.format(account['password']))
        if not find_and_tap('next_btn.png'):
            return
    
    checking_info_screen()

    #tap done
    print('Done')
    if not find_and_tap('done_btn.png'):
        return


def sign_out_google_account():
    # tap google maps
    print('tap google maps')
    if not find_and_tap('google_maps_icon.png'):
        return

    # tap user icon
    print('tap user icon')
    if not find_and_tap('sign_in_user_icon.png'):
        return

    # tap sign out google account
    print('sign out')
    if not find_and_tap('sign_out_btn.png'):
        return

# sign_in_google_account()