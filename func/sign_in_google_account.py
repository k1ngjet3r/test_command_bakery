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
import json
from img_search import image_search, tap_xy

def sign_in_google_account():
    with open('json\\google_account.json') as ac:
        account = json.load(ac)
    
    # takes a screenshot and locate the Google Maps icon
    
