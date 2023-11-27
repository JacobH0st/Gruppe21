import tkinter as tk
from ui_components.base_layout import BaseLayout

class AdminLayout(BaseLayout):
    def setup_ui(self):
        super().setup_ui()
        self.delete_guide_button = tk.Button(self, text="Slett guides", command=self.app.show_admin_marketplace)
        self.delete_guide_button.pack(pady=5)