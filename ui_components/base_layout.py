import tkinter as tk

class BaseLayout(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.setup_ui()
    
    def setup_ui(self):
        self.view_button = tk.Button(self, text="Markedsplass", command=self.app.show_user_marketplace)
        self.view_button.pack(pady=5)
        
        self.back_button = tk.Button(self, text="Tilbake", command=self.app.setup_mode_selection)
        self.back_button.pack(side="bottom")