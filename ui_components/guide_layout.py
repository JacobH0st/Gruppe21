import tkinter as tk
from functions import create_data_entry_form
from ui_components import BaseLayout

class GuideLayout(BaseLayout):
    def setup_ui(self):
        super().setup_ui()
        add_guide_button = tk.Button(self, text="Legg til guide", command=self.app.show_create_data_entry_form)
        add_guide_button.pack(pady=5)