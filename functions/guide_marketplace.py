import tkinter as tk
from functions import MarketplaceBase

class GuideMarketplace(MarketplaceBase):
    def setup_ui(self):
        super().setup_ui()
        
        edit_button = tk.Button(self.frame, text="Endre", command=self.change_existing_guide)
        edit_button.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
    
    def change_existing_guide(self):
        #TODO: gjør det mulig for en guide å endre eksisterende guider
        #TODO: la en guide kunne slette sin egen guide (?), må ha en identifisere til fremtiden, slik at en guide ikke kan slette en annens guide, kun sin egen.
        pass