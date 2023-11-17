import tkinter as tk
from ui_components import BaseLayout

class GuideLayout(BaseLayout):
    def setup_ui(self):
        super().setup_ui()
        add_guide_button = tk.Button(self, text="Legg til guide", command=self.app.show_guide_marketplace)
        add_guide_button.pack(pady=5)