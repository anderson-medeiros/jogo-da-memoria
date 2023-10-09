import tkinter as tk
from tkinter import ttk

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

def log(event):
    print(event)


for i in range(4):
    window.columnconfigure(i, weight=1, minsize=30)
    window.rowconfigure(i, weight=1, minsize=30)
    for j in range(4):
        box = tk.Label(window, bg='black')
        box.grid(column=j, row=i, padx=5, pady=5, ipadx=10, ipady=10, sticky='nsew')


window.mainloop()
