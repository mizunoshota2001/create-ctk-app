import customtkinter as ctk
from components import BasePage


class Labels:
    def __init__(self, page: BasePage):
        ctk.CTkLabel(
            page.frame,
            text="This page is a sample of componentization.       ",
            font=("Courier New", 15, "bold")
        ).grid()
        ctk.CTkLabel(
            page.frame,
            text="Please check the source at app/sample/__init__.py",
            font=("Courier New", 15, "bold")
        ).grid(pady=(0, 20))
