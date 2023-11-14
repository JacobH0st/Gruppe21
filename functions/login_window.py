import tkinter as tk

from functions.create_data_entry_form import create_data_entry_form
from functions.view_data_from_json import view_data_from_json

class LoginWindow(tk.Toplevel): 
    def __init__(self, base_layout):
        super().__init__(base_layout)
        self.base_layout = base_layout
        self.mode = None
        self.initialize_ui()

    def choose_mode(self):
        self.base_layout.deiconify()
        self.destroy()

    def initialize_ui(self):
        self.title("Turisme marketsplass")
        self.geometry("700x500")
        
        self.main_text_label = tk.Label(self, text="")
        self.main_text_label.grid(row=0, column=0, padx=10, pady=10)

        if self.mode == "guide":
            self.main_text_label.config(text="Guide Version:")
            
            self.add_button = tk.Button(self, text="Legg til guide", command=lambda: create_data_entry_form(self))
            self.add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
        elif self.mode == "user" or self.mode is None:
            self.main_text_label.config(text="User Version:")

        view_button = tk.Button(self, text="Marketsplass", command=lambda: view_data_from_json(self))
        view_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)
        
        back_button = tk.Button(self, text="Tilbake", command=self.choose_mode)
        back_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

    def switch_mode(self, new_mode):
        self.mode = new_mode
        self.initialize_ui()
