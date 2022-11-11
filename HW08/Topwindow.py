import tkinter as tk

import Controller
import Model 
from Interfase import Size


add_window:tk.Tk
Change_window:tk.Tk
add_entry:[]=[]
Change_entry:[]=[]


def createAddWindow():
    global add_window
    global add_entry

   
    RESIZEBLE = False

    add_window = tk.Toplevel()
    add_window.title('Добвать контакт')
    add_window.geometry(Size.window_geometry(add_window,Size.AWW, Size.AWH))
    add_window.resizable(RESIZEBLE,RESIZEBLE)
    add_window.wm_attributes('topmost', 1)

    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_label = tk.Label(add_window, text = 'Имя')
    phone_label = tk.Label(add_window, text='Телефон')
    comment_label = tk.Label(add_window, text='Комментарий')
    name_label.grid(column=0,row=0, sticky='e')
    phone_label.grid(column=0,row=1, sticky='e')
    comment_label.grid(column=0,row=2, sticky='e')

    add_entry = [tk.Entry(add_window,width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Добавить', command=lambda: add_contact(add_entry))
    add_button.grid(columnspan=2, row=3)

    add_window.mainloop()

def add_contact(add_entry: list):
    global add_window


    Model.my_phonebook.add(add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    Controller.refresh_table()
    add_window.destroy()