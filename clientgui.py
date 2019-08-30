import client
import json
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox as msg_box
from tkinter.font import Font

CURRENT_DIRECTORY = os.getcwd() + '/'

master = tk.Tk()
master.title('1776 Chatroom')
master.tk.call('wm', 'iconphoto', master._w, tk. PhotoImage(file=CURRENT_DIRECTORY + 'icon.png'))
master.resizable(0, 0)

CLIENT_FONT = Font(master, family='MotoyaLMaru')

"""     BEING FUNCTION DEFINITIONS      """


def load_settings():
    settings_file = open(CURRENT_DIRECTORY + 'settings.json', 'r')
    try:
        json_font = json.load(settings_file)['CLIENT_FONT']
        CLIENT_FONT.config(family=json_font['family'], size=json_font['size'], weight=json_font['weight'],
                           slant=json_font['slant'], underline=json_font['underline'],
                           overstrike=json_font['overstrike'])
    except json.decoder.JSONDecodeError:
        print("No font settings found")


def connect():
    try:
        master.withdraw()
        client.client(ip=ip_address.get(), port=port.get(), username=username_entry.get(), font=CLIENT_FONT)

    except Exception as e:
        msg_box.showerror('General Error ', str(e))


def apply_settings():
    CLIENT_FONT.config(family=font_family_combobox.get(), size=font_size_combobox.get(),
                       weight=bold_val.get(),
                       slant=italic_val.get())
    settings_file = open(CURRENT_DIRECTORY + 'settings.json', 'r')
    json_font = json.load(settings_file)
    settings_file.close()
    json_font['CLIENT_FONT']['family'] = font_family_combobox.get()
    json_font['CLIENT_FONT']['size'] = font_size_combobox.get()
    json_font['CLIENT_FONT']['weight'] = bold_val.get()
    json_font['CLIENT_FONT']['slant'] = italic_val.get()
    json_font['CLIENT_FONT']['underline'] = 0
    json_font['CLIENT_FONT']['overstrike'] = 0

    settings_file = open(CURRENT_DIRECTORY + 'settings.json', 'w')
    json.dump(json_font, settings_file)
    settings_file.close()


def test_text():
    text_test_label.config(
        font=Font(family=font_family_combobox.get(), size=font_size_combobox.get(), weight=bold_val.get(),
                  slant=italic_val.get()))


# exit gui cleanly
def _quit():
    master.quit()
    master.destroy()
    exit()


"""     END FUNCTION DEFINITIONS      """

load_settings()

"""     BEING CONNECTION GUI      """

connect_to_frame = tk.LabelFrame(master, text=' Connect ', font=CLIENT_FONT)
connect_to_frame.grid(column=0, row=0, padx=8, pady=8)

ip_and_port_frame = tk.LabelFrame(connect_to_frame, text='IP and Port configuration', font=CLIENT_FONT)
ip_and_port_frame.grid(column=0, row=0, padx=2, pady=2)

ip_address_label = tk.Label(ip_and_port_frame, anchor=W, text='IP address', font=CLIENT_FONT)
ip_address_label.grid(column=0, row=0)

ip_address = tk.StringVar()
ip_address_box = ttk.Entry(ip_and_port_frame, width=10, textvariable=ip_address)
ip_address_box.grid(column=0, row=1, padx=8, pady=8, sticky=W)

port_label = tk.Label(ip_and_port_frame, anchor=W, text='Port', font=CLIENT_FONT)
port_label.grid(column=1, row=0)

port = tk.IntVar()
port_box = ttk.Entry(ip_and_port_frame, width=5, textvariable=port)
port_box.grid(column=1, row=1, padx=8, pady=8, sticky=W)


username_label = tk.Label(connect_to_frame, text='Username')
username_label.grid(column=0, row=1, padx=2, pady=2)


username = StringVar()
username_entry = tk.Entry(connect_to_frame, textvariable=username, width=24)
username_entry.grid(column=0, row=2, padx=2, pady=2)


connect_button = tk.Button(connect_to_frame, text='Connect!', font=CLIENT_FONT, command=connect)
connect_button.grid(column=0, row=3, padx=4, pady=4)


"""     END CONNECTION GUI      """

"""     BEGIN SETTINGS GUI      """

settings_frame = tk.LabelFrame(master, text=' User settings ', font=CLIENT_FONT)
settings_frame.grid(column=1, row=0, padx=8, pady=8)

font_list = list(font.families())
font_list.sort()

text_settings_frame = tk.LabelFrame(settings_frame, text=' Text ', font=CLIENT_FONT)
text_settings_frame.grid(column=0, row=0, padx=2, pady=2)

font_family_combobox = ttk.Combobox(text_settings_frame, justify=LEFT, width=16, state='readonly')
font_family_combobox['values'] = font_list
font_family_combobox.grid(column=0, row=0, padx=2, pady=2)
font_family_combobox.current(0)

font_size_combobox = ttk.Combobox(text_settings_frame, justify=RIGHT, width=3, state='readonly')
font_size_combobox['values'] = list(range(6, 33))
font_size_combobox.grid(column=1, row=0, padx=2, pady=2)
font_size_combobox.current(6)

bold_val = StringVar()
bold_checkbutton = tk.Checkbutton(text_settings_frame, text='Bold', justify=LEFT, variable=bold_val, onvalue='bold',
                                  offvalue='normal', height=1, width=4, font=CLIENT_FONT)
bold_checkbutton.deselect()
bold_checkbutton.grid(column=0, row=1, padx=2, pady=2)

italic_val = StringVar()
italic_checkbutton = tk.Checkbutton(text_settings_frame, text='Italic', justify=RIGHT, variable=italic_val,
                                    onvalue='italic', offvalue='roman', height=1, width=10, font=CLIENT_FONT)
italic_checkbutton.deselect()
italic_checkbutton.grid(column=1, row=1, padx=2, pady=2)

text_test_label = tk.Label(text_settings_frame, anchor=W, text='AaBbYyZz123', font=CLIENT_FONT)
text_test_label.grid(column=0, row=2, padx=2, pady=2)

test_font_button = tk.Button(text_settings_frame, anchor=E, text='Test font', font=CLIENT_FONT, command=test_text)
test_font_button.grid(column=1, row=2, padx=2, pady=2)


apply_settings_button = tk.Button(text_settings_frame, anchor=W, text='Apply', font=CLIENT_FONT, command=apply_settings)
apply_settings_button.grid(column=0, row=3, padx=2, pady=2)

"""     END SETTINGS GUI      """

"""     QUIT BUTTON     """

quit_button = tk.Button(master, text='Quit', anchor=W, font=CLIENT_FONT, command=_quit)
quit_button.grid(column=0, row=1, padx=2, pady=2)
master.mainloop()
