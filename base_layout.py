import tkinter as tk
from tkinter import *

from functions.create_data_entry_form import create_data_entry_form


def home(self):
    self.title("Turisme marketsplass")
    self.geometry("500x500")
    add_button = tk.Button(self, text="Forms", command=create_data_entry_form)
    add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()
        
        home(self)

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()