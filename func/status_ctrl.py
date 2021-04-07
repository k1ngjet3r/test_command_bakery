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

    steps = [
        'google_maps_icon.png',
        'sign_out_user_icon.png',
        'sign_in_to_google_text.png',
        'sign_in_on_car_screen.png',
        'username_entry_field.png',
        'password_entry_field.png',
        'done_btn.png'
    ]

    i = 0

    while i < len(steps):
        print('[Sign-In] {}'.format(steps[i][:-4]))
        progress = find_and_tap(steps[i])
        if progress:
            checking_info_screen()
            if steps[i][-9:-4] == 'field' and steps[i][:8] == 'username':
                print('[DEBUG] entering username')
                os.system('adb shell input text "{}"'.format(account['username']))
                time.sleep(2)
                find_and_tap('next_btn.png')
            elif steps[i][-9:-4] == 'field' and steps[i][:8] == 'password':
                print('[DEBUG] entering password')
                os.system('adb shell input text "{}"'.format(account['password']))
                time.sleep(2)
                find_and_tap('next_btn.png')
            i += 1
        else:
            print('[Error] Fail on step {}'.format(steps[i][:-4]))
            break

        time.sleep(3)

    # # tap google maps
    # print('tap google maps')
    # tap_google_maps = find_and_tap('google_maps_icon.png')
    # if not tap_google_maps:
    #     return

    # # tap user icon
    # print('tap user icon')
    # tap_user_icon = find_and_tap('sign_out_user_icon.png')
    # if not tap_user_icon:
    #     return
    
    # checking_info_screen()

    # # tap sign in to google 
    # print('tap sign in')
    # tap_sign_in = find_and_tap('sign_in_to_google_text.png')
    # if not tap_sign_in:
    #     return
    
    # checking_info_screen()

    # # sing in on car screen
    # print('tap sign in on car screen')
    # tap_sign_in_on_car = find_and_tap('sign_in_on_car_screen.png')
    # if not tap_sign_in_on_car:
    #     return

    # checking_info_screen()

    # # tap username entry field and enter username
    # print('tap username entry fielf and enter username')
    # tap_un_entry = find_and_tap('username_entry_field.png')
    # if not tap_un_entry:
    #     return
    # else:
    #     os.system('adb shell input text "{}"'.format(account['username']))
    #     if not find_and_tap('next_btn.png'):
    #         return
    
    # checking_info_screen()

    # # tap password entry field and enter password
    # print('tap password entry field and enter password')
    # tap_pw_entry = find_and_tap('password_entry_field.png')
    # if not tap_pw_entry:
    #     return
    # else:
    #     os.system('adb shell input text "{}"'.format(account['password']))
    #     if not find_and_tap('next_btn.png'):
    #         return
    
    # checking_info_screen()

    # #tap done
    # print('Done')
    # done = find_and_tap('done_btn.png')
    # if not done:
    #     return


def sign_out_google_account():
    steps = ['google_maps_icon.png', 
            'sign_in_user_icon.png',
            'sign_out_btn.png',
            ]
    
    i = 0

    while i < len(steps):
        print('[Sign-In] {}'.format(steps[i][:-4]))
        progress = find_and_tap(steps[i])
        if not progress:
            print('[Error] Fail on step {}'.format(steps[i][:-4]))
            break
        else:
            i += 1

    
    # # tap google maps
    # print('tap google maps')
    # if not find_and_tap('google_maps_icon.png'):
    #     return

    # # tap user icon
    # print('tap user icon')
    # if not find_and_tap('sign_in_user_icon.png'):
    #     return

    # # tap sign out google account
    # print('sign out')
    # if not find_and_tap('sign_out_btn.png'):
    #     return

# sign_out_google_account()