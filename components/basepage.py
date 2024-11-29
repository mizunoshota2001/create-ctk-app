import customtkinter as ctk


class BasePage:
    def __init__(self, master: ctk.CTk):
        self.master = master
        [child.destroy() for child in self.master.winfo_children()]
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.frame = ctk.CTkFrame(self.master, fg_color="transparent")

    def render(self):
        pass


