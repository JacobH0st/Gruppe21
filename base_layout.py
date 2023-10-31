import tkinter as tk
from tkinter import *
from functions.login_window import LoginWindow
import functions.view_data_from_json
from functions.create_data_entry_form import create_data_entry_form

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mode = None
        self.choose_mode()

    def choose_mode(self):
        mode_selection_window = LoginWindow(self)
        mode_selection_window.mainloop()

    def initialize_ui(self):
        self.title("Turisme marketsplass")
        self.geometry("700x500")
        
        self.main_text_label = Label(self, text="")
        self.main_text_label.grid(row=0, column=0, padx=10, pady=10)

        if self.mode == "guide":
            self.main_text_label.config(text="Guide Version:")
            
            self.add_button = Button(self, text="Legg til guide", command= lambda: create_data_entry_form(self))
            self.add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
        elif self.mode == "user" or self.mode is None:
            self.main_text_label.config(text="User Version:")
            #ERROR HVIS BRUKER VELGER USER FØR GUIDE
            ##self.add_button.grid_remove()
            pass

        view_button = Button(self, text="Marketsplass", command=lambda: functions.view_data_from_json.view_data_from_json(self))
        view_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)
        
        ##TODO FIKSE BACK BUTTON
        ##back_button = Button(self, text="Tilbake", command=self.choose_mode)
        ##back_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

    def switch_mode(self, new_mode):
        self.mode = new_mode
        self.initialize_ui()
        
    def goBack(self):
        self.initialize_ui()

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()