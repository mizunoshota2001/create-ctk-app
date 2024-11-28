import customtkinter as ctk
from components import BasePage
import webbrowser


class Page(BasePage):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)

    def render(self):
        ctk.set_default_color_theme("dark-blue") 
        ctk.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        frame = ctk.CTkFrame(self.master,fg_color="transparent")
        frame.grid(sticky="ew")

        frame.grid_columnconfigure(0, weight=1)

        _ctk_url = "https://customtkinter.tomschimansky.com/"
        _github_url = "https://github.com/mizunoshota2001/create-ctk-app"

        ctk.CTkLabel(
            frame,
            text="CreateCTkApp",
            font=("Comic Sans MS", 50, "bold")
        ).grid(pady=(0, 20))
        ctk.CTkLabel(
            frame,
            text="1. Get started by editing app/top/__init__.py",
            font=("Courier New", 15, "bold")
        ).grid()
        ctk.CTkLabel(
            frame,
            text="2. Restart main.py after saving the file     ",
            font=("Courier New", 15, "bold")
        ).grid(pady=(0, 20))
        ctk.CTkButton(
            frame,
            text="▲ Read CTk documentation",
            corner_radius=999,
            font=("Arial", 15, "bold"),
            height=40,
            command=lambda: webbrowser.open(_ctk_url)
        ).grid(pady=(0, 10))
        ctk.CTkButton(
            frame, text="See the sources",
            corner_radius=999,
            font=("Arial", 15, "bold"),
            height=40,
            command=lambda: webbrowser.open(_github_url)
        ).grid()
