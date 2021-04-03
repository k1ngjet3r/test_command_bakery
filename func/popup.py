import tkinter as tk

def Popup(master=window):
    popup = tk.Toplevel(master)
    popup.title('Pop-up')
    popup.geometry('200x200')
    popup_lbl = tk.Label(popup, text='This is a popup!').pack()
