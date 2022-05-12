import random
from tkinter import *
root = Tk()
root.geometry("700x500")
l1 = Label(root, font=("bold",200))
def rolldice():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()
b1 = Button(root, text="click here..",command= rolldice)
b1.place(x = 320, y = 0)
root.mainloop()
