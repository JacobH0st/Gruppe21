import tkinter as tk
from tkinter import *


def home(self):
    self.title("Turisme marketsplass")
    self.geometry("500x500")

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()
        
        home(self)

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()