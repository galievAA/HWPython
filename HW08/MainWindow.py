import tkinter as tk
from tkinter import ttk

from Interface import Size

main_window: tk.Tk
main_label: tk.Label
add_entry:[]
main_table: ttk.Treeview

def main():

    global main_window

    RESIZEBLE = False

    main_window = tk.Tk() # создаем окно
    main_window.title('Телефонный справочник')
    main_window.geometry(Size.winndow_geometry(main_window, Size.MWW,Size.MWH))
    main_window.resizeable(RESIZEBLE,RESIZEBLE)
    main_window.wm_attributes('-topmost',1)


    main_table = ttk.Treeview(main_window, show = 'headings')
    heads = ['id', 'Имя', 'Телефон', 'Комментарий']
    main_table['colums'] = heads
    for header in heads:
        main_table.heading(header, text=header,anchor='w')

    main_table.pack()
    add_button = tk.Button(main_window, text='Добавить', command=open_add_window)
    add_button.pack()



    main_window.mainloop() # его зацикливает 

def open_add_window():
    TopWindow.createAddWindow()
    #pass # заглушка