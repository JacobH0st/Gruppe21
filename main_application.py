import tkinter as tk
from functions import AdminMarketplace, GuideMarketplace, UserMarketplace, CreateDataEntryFormBase
from ui_components import AdminLayout, GuideLayout, UserLayout

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turisme Markedsplass")
        self.geometry("700x500")
        self.current_mode = None

        self.main_frame = tk.Frame(self)
        self.data_entry_frame = tk.Frame(self)
        self.marketplace_frame = tk.Frame(self)

        self.setup_mode_selection()
        self.main_frame.pack()

    def setup_mode_selection(self):
        self.clear_frame(self.main_frame)
        self.geometry("700x500")
        
        mode_label = tk.Label(self.main_frame, text="Velg modus:")
        mode_label.pack(pady=10)
        
        for mode in ["User", "Guide", "Admin"]:
            button = tk.Button(self.main_frame, text=f"{mode} Modus", command=lambda m=mode: self.show_buttons(m))
            button.pack(pady=5)
            
    def open_data_entry_form(self):
        self.main_frame.pack_forget()
        self.geometry("300x500")
        
        self.data_entry_frame.pack()
        
    def switch_to_main_frame(self):
        self.data_entry_frame.pack_forget()
        self.marketplace_frame.pack_forget()
        self.geometry("700x500")
        self.main_frame.pack()
        
    def show_marketplace(self, marketplace_class):
        self.main_frame.pack_forget()
        self.geometry("1920x1080")
        self.current_marketplace = marketplace_class(self)
        self.current_marketplace.frame.pack()
        
    def show_data_entry_form(self, create_data_entry_form_class):
        self.main_frame.pack_forget()
        self.geometry("700x500")
        self.entry_form = create_data_entry_form_class(self, self.data_entry_frame)
        self.entry_form.frame.pack()


    def show_user_marketplace(self):
        self.show_marketplace(UserMarketplace)
        
    def show_guide_marketplace(self):
        self.show_marketplace(GuideMarketplace)

    def show_admin_marketplace(self):
        self.show_marketplace(AdminMarketplace)
    
    def show_create_data_entry_form(self):
        self.show_data_entry_form(CreateDataEntryFormBase)
        
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


    def show_buttons(self, mode):
        self.clear_frame(self.main_frame)
        self.current_mode = mode
        
        label = tk.Label(self.main_frame, text=f"{mode} Modus")
        label.pack(pady=10)
        
        if mode == "User":
            self.layout = UserLayout(self.main_frame, self)
        elif mode == "Guide":
            self.layout = GuideLayout(self.main_frame, self)
        elif mode == "Admin":
            self.layout = AdminLayout(self.main_frame, self)
        
        self.layout.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
