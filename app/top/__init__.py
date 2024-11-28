import customtkinter as ctk
from app import sub
from components import BasePage


class Page(BasePage):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)

    def render(self):
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        frame = ctk.CTkFrame(self.master)
        frame.grid(sticky="nsew")

        frame.grid_rowconfigure((0, 1, 2), weight=1)
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(frame,
                     text="Hello, world!")\
            .grid(sticky="nsew")

        button = ctk.CTkButton(frame, text="my button",
                               command=lambda: print("button clicked"))
        button.grid(sticky="nsew")

        switch_button = ctk.CTkButton(
            frame, text="別のフレームに切り替え", command=lambda: self.replace(sub.Page(self.master)))
        switch_button.grid(sticky="nsew")
