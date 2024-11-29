import customtkinter as ctk
from components import BasePage
import lib.sample


class Title:
    def __init__(self, page: BasePage):
        text = lib.sample.getHelloWorld()
        ctk.CTkLabel(
            page.frame,
            text=text,
            font=("Comic Sans MS", 50, "bold")
        ).grid(pady=(0, 20))
