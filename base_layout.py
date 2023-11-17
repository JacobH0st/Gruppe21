import tkinter as tk
from functions.view_data_from_json import view_data_from_json
from functions.create_data_entry_form import create_data_entry_form

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turisme Markedsplass")
        self.geometry("700x500")
        self.chosenMode = None

        self.main_frame = tk.Frame(self)
        self.data_entry_frame = tk.Frame(self)
        self.view_json_frame = tk.Frame(self)  # Frame for viewing JSON data

        self.setup_mode_selection()
        self.main_frame.pack()  # Ensure the main frame is packed initially

    def setup_mode_selection(self):
        self.clear_frame(self.main_frame)
        self.geometry("700x500")
        mode_label = tk.Label(self.main_frame, text="Velg modus:")
        mode_label.pack(pady=10)
        
        for mode in ["User", "Guide", "Admin"]:
            button = tk.Button(self.main_frame, text=f"{mode} Modus", command=lambda m=mode: self.show_buttons(m))
            button.pack(pady=5)
            
        #self.setLoginMode()   
            
    def open_data_entry_form(self):
        self.main_frame.pack_forget()
        self.view_json_frame.pack_forget()
        self.geometry("300x500")
        create_data_entry_form(self, self.data_entry_frame)
        self.data_entry_frame.pack()
        
    def switch_to_main_frame(self):
        self.data_entry_frame.pack_forget() # fjerner 
        self.view_json_frame.pack_forget() # fjerner
        self.geometry("700x500")
        self.main_frame.pack()
        
    def open_view_json_frame(self):
        self.main_frame.pack_forget()
        self.data_entry_frame.pack_forget()
        self.geometry("1920x1080")
        view_data_from_json(self, self.view_json_frame)
        self.view_json_frame.pack()


    def show_buttons(self, mode):
        self.clear_frame(self.main_frame)
        label = tk.Label(self.main_frame, text=f"{mode} Modus")
        label.pack(pady=10)
        
        
        add_button = tk.Button(self.main_frame, text="Legg til guide", command=lambda: self.open_data_entry_form())
        add_button.pack(pady=5)
        
        if mode == "User":
            add_button.destroy() 
            
        if mode == "Admin":
            delete_button = tk.Button(self.main_frame, text="Slett guides", command=lambda: self.open_view_json_frame())
            delete_button.pack(pady=5)

        view_button = tk.Button(self.main_frame, text="Markedsplass", command=lambda: self.open_view_json_frame())
        view_button.pack(pady=5)

        back_button = tk.Button(self.main_frame, text="Tilbake", command=self.setup_mode_selection)
        back_button.pack(side="bottom")

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
