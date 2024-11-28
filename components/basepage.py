import customtkinter as ctk


class BasePage:
    def __init__(self, master: ctk.CTk):
        self.master = master

    def render(self):
        pass

    def replace(self, page: "BasePage"):
        [child.destroy() for child in self.master.winfo_children()]
        page.render()
