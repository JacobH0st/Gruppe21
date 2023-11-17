import tkinter as tk
from functions import MarketplaceBase

class AdminMarketplace(MarketplaceBase):
    def setup_ui(self):
        super().setup_ui()
        
        delete_button = tk.Button(self.frame, text="Slett", command=self.delete_existing_guide)
        delete_button.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
    
    def delete_existing_guide(self):
        #TODO: gjør det mulig for en guide å endre eksisterende guider
        #TODO: la en admin kunne slette guider.
        pass