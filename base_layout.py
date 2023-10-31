import tkinter as tk
from tkinter import *
import functions.view_data_from_json
import functions.create_data_entry_form

class LoginWindow(tk.Toplevel):
    def __init__(self, base_layout):
        super().__init__()
        self.base_layout = base_layout
        self.title("Login")
        self.geometry("300x150")
        
        self.label = tk.Label(self, text="Select your mode:")
        self.label.pack(pady=10)
        
        self.user_button = tk.Button(self, text="User Mode", command=self.login_as_user)
        self.user_button.pack(pady=5)
        
        self.guide_button = tk.Button(self, text="Guide Mode", command=self.login_as_guide)
        self.guide_button.pack(pady=5)

    def login_as_user(self):
        self.base_layout.mode = "user"
        self.base_layout.initialize_ui()
        self.destroy()

    def login_as_guide(self):
        self.base_layout.mode = "guide"
        self.base_layout.initialize_ui()
        self.destroy()

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
        self.geometry("500x500")

        if self.mode == "guide":
            add_button = Button(self, text="Forms", command=lambda: functions.create_data_entry_form.create_data_entry_form)
            add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
        elif self.mode == "user" or self.mode is None:
            pass  # Adjust this as needed for user mode

        view_button = Button(self, text="Marketplace", command=lambda: functions.view_data_from_json.view_data_from_json(self))
        view_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

    def switch_mode(self, new_mode):
        self.mode = new_mode
        self.initialize_ui()

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()
