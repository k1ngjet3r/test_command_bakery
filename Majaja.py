'''
    Welcome to version 2.1.0

    Created by: Jeter Lin

    Adding new image recognition for system setting-related task accuracy

    Current function including internet conncetion control, google account login or out control, create user, and Google Assistant command sender

    If this is your first time using Majaja, there are few things that you need to do:
    1. Go to \json folder and create google_account.json to store google account's username and password
    2. Create a folder named "temp" in the \img folder
    
'''

import subprocess
from tkinter import StringVar, ttk
from func.adb_command import online, offline, pin_lock, pw_lock, pattern_lock, screenshot, check_adb_status
from PIL import Image, ImageTk
import tkinter as tk
import os
import json
from func.img_and_audio import img_selector, audio_selector
from func.tts_engine import activate_ga, tts, hey_google_cmd, adb_cmd
from playsound import playsound
# from func.status_ctrl import sign_out_google_account
from func.media_ctrl import play_pause, next_act, previous_act
from tkinter import messagebox
import time
from func.img_search import find_and_tap, checking_screen
# from func.popup import Popup

img_directory = img_selector()

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
    ]

    i = 0

    color.set('blue')
    v.set('Signing In, Please Wait!')

    while i < len(steps):
        color.set('blue')
        v.set(steps[i][:-4])
        print('[Sign-In] {}'.format(steps[i][:-4]))
        progress = find_and_tap(steps[i])
        
        if progress == False:
            print('[Error] Fail on step {}'.format(steps[i][:-4]))
            color.set('red')
            v.set('Something Went Wrong!')
            break
        else:
            time.sleep(2)
            checking_screen('checking_info_text.png')
            if steps[i][-9:-4] == 'field' and steps[i][:8] == 'username':
                color.set('blue')
                v.set('Entering Username')
                print('[DEBUG] entering username')
                os.system('adb shell input text "{}"'.format(account['username']))
                time.sleep(1)
                find_and_tap('next_btn.png')
                checking_screen('signing_pending_screen.png')

                time.sleep(5)
                color.set('blue')
                v.set('Entering Password')
                print('[DEBUG] entering password')
                os.system('adb shell input text "{}"'.format(account['password']))
                time.sleep(3)
                find_and_tap('next_btn.png')
                checking_screen('signing_in_text.png')
            i += 1
    else:
        print('[DEBUG] Signin Successful!')
        color.set('green')
        v.set('DONE!')

def sign_out_google_account():
    steps = ['google_maps_icon.png', 
            'sign_in_user_icon.png',
            'sign_out_btn.png',
            ]
    
    i = 0

    color.set('blue')
    v.set('Signing Out, Please Wait!')
    
    while i < len(steps):
        color.set('blue')
        v.set(steps[i][:-4])
        print('[Sign-In] {}'.format(steps[i][:-4]))
        progress = find_and_tap(steps[i])
        if progress == False:
            print('[Error] Fail on step {}'.format(steps[i][:-4]))
            color.set('red')
            v.set('Something Went Wrong!')
            break
        else:
            i += 1
            time.sleep(2)
    else:
        print('[DEBUG] Sign Out Successful!')
        color.set('green')
        v.set('DONE!')

def creat_user():
    name = user_enrty.get()
    name = name.replace(' ', '\\ ')
    frame = 'adb shell pm create-user '
    cmd = frame + name
    os.system('adb root')
    os.system(cmd)
    print(cmd)

def exe_command():
    mode = mode_var.get()
    # query = query_listbox.get(query_listbox.curselection())
    type_query = type_query_field.get()
    mode_list = ['Speech Mode', 'Majami Mode']

    # print(type_query)
    # print(type_query == None)
    # print(type_query == '')

    print('[MODE] {}'.format(mode_list[mode-1]))

    # if user selected "speech mode"
    if mode == 1:
        # if user checked the hey google checkbox
        if var_hey_google.get() == 1:
            # if user did not enter any query
            if type_query == '':
                query = query_listbox.get(query_listbox.curselection())
                print('[HeyGoogle/TTS] {}'.format(query))
                hey_google_cmd(query)

            # if user entered the query by themselve
            elif type_query != '':
                print('[HeyGoogle/Typed/TTS] {}'.format(type_query))
                hey_google_cmd(type_query)
            
        # if user did not checked the hey google checkbox
        elif var_hey_google.get() == 0:
            # if user entered the query by themselve
            if type_query != '':
                print('[Typed/TTS] {}'.format(type_query))
                adb_cmd(type_query)
            # if user did not enter any query
            elif type_query == '':
                query = query_listbox.get(query_listbox.curselection())
                print('[TTS] {}'.format(query))
                adb_cmd(query)
    
    # if user selected "Majami mode"
    elif mode == 2:
        # if user did not enter any query
        if type_query == '':
            query = query_listbox.get(query_listbox.curselection())
            query = query.replace(' ', '\\ ')
            frame = 'adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity -e query '
            frame = frame.split()
            print('[ADB] {}'.format(frame+query))
            # adb_query = frame.append(query)
            # subprocess.check_output(adb_query)
            os.system(frame+query)
            

        # if user entered the query by themselve
        elif type_query != '':
            query = type_query.replace(' ', '\\ ')
            frame = 'adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity -e query '
            print('[ADB] {}'.format(frame+query))
            # adb_query = frame.append(query)
            # subprocess.check_output(adb_query)
            os.system(frame+query)

def on_select(event):
    # print('[DEBUG] event: ', event)
    # print('[DEBUG] event.widget: ', event.widget)
    # print('[DEBUG] event.widget.get(): ', event.widget.get())

    selected = event.widget.get()

    # Load and read the command JSON file
    with open('json\\function_value.json') as json_file:
        combobox_values = json.load(json_file)

    query_listbox.delete(0, 'end')
    for item in combobox_values[selected]:
        query_listbox.insert('end', item)

def security_setting():
    security_type = security_combobox.get()
    print('[SECURITY] setting security type: {}'.format(security_type))
    if security_type == 'PIN':
        pin_lock()
    elif security_type == 'Password':
        pw_lock()
    elif security_type == 'Pattern':
        pattern_lock()

def adb_status():
    # Checking adb status
    if check_adb_status():
        v.set('Ready')
        color.set('green')
    else:
        v.set('OH NO~\nOH NO~\nOH NO~')
        color.set('red')

common_fg = 'white'
common_bg = 'grey25'

window = tk.Tk()
window.title("MAJAJA v2.1.0 Beta")
window.resizable(False, False)

'''
    Frame that hold image
'''
img_frame = tk.Frame(window, width=500, height=200, bg=common_bg)
img_frame.pack(side=tk.LEFT, fill=tk.Y)
selected_image = Image.open(img_directory)
selected_image = selected_image.resize((240, 180), Image.ANTIALIAS)
img = ImageTk.PhotoImage(selected_image)
panel = tk.Label(img_frame, image=img, bg=common_bg, fg=common_fg)
panel.pack()

# mode-selection frame
mode_frame = tk.Frame(img_frame, bg=common_bg)
mode_frame.pack()

mode_var = tk.IntVar(None, 1)

speech_mode = tk.Radiobutton(mode_frame, text='Speech Mode', variable=mode_var, value=1, bg=common_bg, fg=common_fg, activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg, font='Helvetica 10 bold')
speech_mode.pack(side=tk.LEFT)

Majami_mode = tk.Radiobutton(mode_frame, text='Majami Mode', variable=mode_var, value=2, bg=common_bg, fg=common_fg, activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg, font='Helvetica 10 bold')
Majami_mode.pack(side=tk.LEFT)

'''
    Frame that hold connection and sign status control
'''
connection_sign_frame = tk.Frame(window, width=500, bg=common_bg)
connection_sign_frame.pack(side=tk.LEFT, fill=tk.Y)

status_label = tk.Label(connection_sign_frame, text='Status Control', width=19, font='Helvetica 10 bold', bg=common_bg, fg='goldenrod1')
status_label.pack()


connection_frame = tk.Frame(connection_sign_frame, borderwidth=2, relief='groove', bg=common_bg)
connection_frame.pack(side=tk.TOP)

connection_lebel = tk.Label(connection_frame, text='Connection', width=20, font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
connection_lebel.pack()

connection_var = [
    ("Online", 1, online),
    ("Offline", 2, offline)]

connection_v = tk.IntVar()

for connection, num, cmd in connection_var:
    connection_rb = tk.Radiobutton(
        connection_frame, text=connection, variable=connection_v, value=num, command=cmd, bg=common_bg, fg=common_fg, activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg)
    connection_rb.pack(side=tk.LEFT)

sep= tk.Frame(connection_sign_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

sign_frame = tk.Frame(connection_sign_frame, borderwidth=2, relief='groove', bg=common_bg)
sign_frame.pack(side=tk.TOP)

sign_lebel = tk.Label(sign_frame, text='Sign Status', width=20, font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
sign_lebel.pack()

sign_var = [
    ("Sign-In", 1, sign_in_google_account),
    ("Sign-Out", 2, sign_out_google_account)]

sign_v = tk.IntVar()

for status, num, cmd in sign_var:
    sign_rb = tk.Radiobutton(sign_frame, text=status, variable=sign_v, value=num, command=cmd, bg=common_bg, fg=common_fg, activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg)
    sign_rb.pack(side=tk.LEFT)

sep= tk.Frame(connection_sign_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

v = StringVar()
color = StringVar()

adb_status()

msg_lbl = tk.Label(connection_sign_frame, textvariable=v, font='Helvetica 9 bold', bg=common_bg, fg=color.get(), anchor="e", justify=tk.LEFT)
msg_lbl.pack()


'''
    Frame that holds user_related control
'''

user_rlt_frame = tk.Frame(window, bg=common_bg)
user_rlt_frame.pack(side=tk.LEFT, fill=tk.Y)

user_label = tk.Label(user_rlt_frame, text='User/Security Control', width=22, font='Helvetica 10 bold', bg=common_bg, fg='goldenrod1')
user_label.pack()

create_user_frame = tk.Frame(user_rlt_frame, borderwidth=2, relief='groove', bg=common_bg)
create_user_frame.pack(side=tk.TOP, fill='y')
creat_user_lbl = tk.Label(create_user_frame, text='Create New User', width=23 ,font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
creat_user_lbl.pack(side=tk.TOP)
user_name_label = tk.Label(create_user_frame, text='Name:', width=5, bg=common_bg, fg=common_fg)
user_name_label.pack(side=tk.LEFT)
user_enrty = tk.Entry(create_user_frame, width=12, bg='grey', fg=common_fg)
user_enrty.pack(side=tk.LEFT)
user_btn = tk.Button(create_user_frame, text='Create', command=creat_user, width=5, bg='grey', font='Helvetica 9 bold')
user_btn.pack(side=tk.LEFT)

sep= tk.Frame(user_rlt_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

security_frm = tk.Frame(user_rlt_frame, borderwidth=2, relief='groove', bg=common_bg)
security_frm.pack()
security_lbl = tk.Label(security_frm, text='Security Setting', width=23, font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
security_lbl.pack()
security_title_label = tk.Label(security_frm, text='Type:', width=5, bg=common_bg, fg=common_fg)
security_title_label.pack(side=tk.LEFT)
security_combobox = ttk.Combobox(security_frm, values=['PIN', 'Password', 'Pattern'], width=9)
security_combobox.pack(side=tk.LEFT)
security_btn = tk.Button(security_frm, text='Set', width=5, command=security_setting, bg='grey', font='Helvetica 9 bold')
security_btn.pack(side=tk.LEFT)

sep= tk.Frame(user_rlt_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)



'''
    Frame that holds command control
'''

cmd_frame = tk.Frame(window, width=300, bg=common_bg)
cmd_frame.pack(side=tk.LEFT, fill=tk.Y)

cmd_lbl = tk.Label(cmd_frame, text='Query Generator', font='Helvetica 10 bold', width=29, bg=common_bg, fg='goldenrod1')
cmd_lbl.pack()

# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(cmd_frame, bg=common_bg)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function', bg=common_bg, fg=common_fg)
function_label.pack(side=tk.LEFT)

combobox = ttk.Combobox(top_frame, values=['Call Smoke','call FN', 'call LN', 'call location','SMS','Message', 'Navi', 'Radio','Reply', 'Other', 'Media'], width=12)
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select),
var_hey_google = tk.IntVar()
hey_google_checkbox = tk.Checkbutton(top_frame, text='Hey Google', variable=var_hey_google, onvalue=1, offvalue=0, bg=common_bg, fg=common_fg, activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg)
hey_google_checkbox.pack(side=tk.LEFT)

sep= tk.Frame(cmd_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

query_listbox_frame = tk.Frame(cmd_frame, bg=common_bg)
query_listbox_frame.pack(side=tk.TOP)

var = tk.StringVar()
# var.set((1, 2, 3))

query_listbox = tk.Listbox(
    query_listbox_frame, listvariable=var, selectmode=tk.SINGLE, width=35, height=6, bg='grey75')
query_listbox.pack(side=tk.TOP)

# scrollbar = tk.Scrollbar(query_listbox_frame, orient="vertical")
# scrollbar.config(command=query_listbox.yview, background='grey')
# scrollbar.pack(side="left", fill="y")

sep= tk.Frame(query_listbox_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

type_query_field = tk.Entry(query_listbox_frame, width=35, bg='grey', fg=common_fg)
type_query_field.pack(side=tk.TOP)

sep= tk.Frame(cmd_frame, height=6, bg=common_bg)
sep.pack(side=tk.TOP)

send_btn_frame = tk.Frame(cmd_frame, bg=common_bg)
send_btn_frame.pack(side=tk.TOP)

send_btn = tk.Button(send_btn_frame, text='Execute',
                     width=29, command=exe_command, bg='grey', font='Helvetica 9 bold')
send_btn.pack(side=tk.LEFT)


# '''
#     Call, SMS, Navi control frame
# '''

# mulit_frame = tk.Frame(window, bg=common_bg)
# mulit_frame.pack(side=tk.LEFT, fill=tk.Y)
# multi_lbl = tk.Label(mulit_frame, text='Multi Control', font='Helvetica 10 bold', width=29, bg=common_bg, fg='goldenrod1')
# multi_lbl.pack()

# call_frame = tk.Frame(mulit_frame, bg=common_bg, borderwidth=2, relief='groove')
# call_frame.pack()
# call_lbl = tk.Label(call_frame, text='Call', font='Helvetica 10 bold', bg=common_bg, fg=common_fg)
# call_lbl.pack()

# fn_combox = ttk.Combobox(call_frame, width=10)
# fn_combox.pack(side=tk.LEFT)

# ln_combo = ttk.Combobox(call_frame, width=10)
# ln_combo.pack(side=tk.LEFT)

# call_exe_btn = tk.Button(call_frame, text='Send', width=5, bg='grey', font='Helvetica 9 bold')
# call_exe_btn.pack(side=tk.LEFT)
'''
    more control frame
'''
more_ctrl = tk.Frame(window, width=500, bg=common_bg)
more_ctrl.pack(side=tk.LEFT, fill=tk.Y)


media_lbl = tk.Label(more_ctrl, text='Other', width=22, font='Helvetica 10 bold', bg=common_bg, fg='goldenrod1')
media_lbl.pack()

media_ctrl_frm = tk.Frame(more_ctrl, borderwidth=2, relief='groove', bg=common_bg)

media_ctrl_title = tk.Label(media_ctrl_frm, text='Media Control', width=23, font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
media_ctrl_title.pack()
previous_btn = tk.Button(media_ctrl_frm, text=u"\u23EE", bg='grey', font='Helvetica 11 bold', width=5, command=previous_act)
previous_btn.pack(side=tk.LEFT)

play_pause_btn = tk.Button(media_ctrl_frm, text=u"\u23EF", bg='grey', font='Helvetica 11 bold', width=5, command=play_pause)
play_pause_btn.pack(side=tk.LEFT)

next_btn = tk.Button(media_ctrl_frm, text=u"\u23ED", width=5, bg='grey', font='Helvetica 11 bold', command=previous_act)
next_btn.pack(side=tk.LEFT)

media_ctrl_frm.pack()
# max_user_btn = tk.Button(user_rlt_frame, text='Max User')
# max_user_btn.pack()

other_ctrl_frame = tk.Frame(more_ctrl, borderwidth=2, relief='groove', bg=common_bg)
other_ctrl_frame.pack()

other_lbl = tk.Label(other_ctrl_frame, text='Other', width=23, font='Helvetica 9 bold', bg=common_bg, fg=common_fg)
other_lbl.pack()

screenshot_btn = tk.Button(other_ctrl_frame, text='screenshot', command=screenshot, width=19, bg='grey', font='Helvetica 9 bold')
screenshot_btn.pack()


window.call('wm', 'attributes', '.', '-topmost', '1')

# playsound(audio_selector())
window.mainloop()
# playsound('audio\\100_dollar.mp3')