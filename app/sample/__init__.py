import customtkinter as ctk
from components import BasePage
from components.sample import Buttons, Labels, Title


class Page(BasePage):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)

    def render(self):
        self.frame.grid(sticky="ew")
        self.frame.grid_columnconfigure(0, weight=1)

        Title(self)
        Labels(self)
        Buttons(self)
