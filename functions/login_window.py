import tkinter as tk

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