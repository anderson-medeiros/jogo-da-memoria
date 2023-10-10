import tkinter as tk
from tkinter import ttk
from random import shuffle


window = tk.Tk()
window_width = window_height = 500
# obtêm a dimensão da tela
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# calcula o centro
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.title('Jogo da memória')


hexdecimal_colors = [
    '#0000FF',
    '#00FFFF',
    '#00FF7F',
    '#DAA520',
    '#7B68EE',
    '#DC143C',
    '#FF0000',
    '#FF4500'] * 2

shuffle(hexdecimal_colors)
widget_colors = {f'.!label{n + 1 if n else ""}':hexdecimal_colors[n] for n in range(16)}


active_widgets = 0
widget1 = None
widget2 = None

def view_color(event):
    global active_widgets
    active_widgets += 1
    global widget1
    global widget2
    widget = event.widget

    if active_widgets == 1:
        widget1 = widget
    elif active_widgets == 2:
        widget2 = widget


    widget.config(bg=widget_colors[str(widget)])
    if active_widgets > 2:
        active_widgets = 1
        widget1.config(bg='black')
        widget2.config(bg='black')
        widget1 = widget
        widget2 = None


def checker_victory(event):
    global widget1
    global widget2
    if widget_colors.get(str(widget1)) == widget_colors.get(str(widget2)) and widget1 != widget2:
        widget1.grid_remove()
        widget2.grid_remove()




for i in range(4):
    window.columnconfigure(i, weight=1, minsize=30)
    window.rowconfigure(i, weight=1, minsize=30)
    for j in range(4):
        box = tk.Label(window, bg='black')
        box.grid(column=j, row=i, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')
        box.bind('<Button-1>', view_color)
        box.bind('<Button-1>', checker_victory, add='+')


window.mainloop()
