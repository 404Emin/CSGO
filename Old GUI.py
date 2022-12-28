from tkinter import *
import tkinter as tk
from subprocess import call
import Glow
import keyboard

padxbutton = (50)
root = tk.Tk()
root.title("Skill issue")

def glow():
    print()

        

bg = tk.Canvas(root, height=200, width=150, bg="#566573")
bg.pack()


glow_b = tk.Button(bg, text="Glow esp", padx=(padxbutton), pady=7, fg="black", bg="#808B96", command=glow)
glow_b.pack(in_= bg,side=TOP)


root.mainloop()
