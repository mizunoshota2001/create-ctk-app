import customtkinter as ctk
from components import BasePage


class Title:
    def __init__(self, page: BasePage):
        ctk.CTkLabel(
            page.frame,
            text="SamplePage",
            font=("Comic Sans MS", 50, "bold")
        ).grid(pady=(0, 20))
