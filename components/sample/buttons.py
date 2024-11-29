from components import BasePage
import customtkinter as ctk
import webbrowser
import app


class Buttons:
    def __init__(self, page: BasePage):
        _github_url = "https://github.com/mizunoshota2001/create-ctk-app"
        ctk.CTkButton(
            page.frame,
            text="▲ See the sources",
            corner_radius=999,
            font=("Arial", 15, "bold"),
            height=40,
            command=lambda: webbrowser.open(_github_url)
        ).grid(pady=(0, 10))
        ctk.CTkButton(
            page.frame, text="Back to the top page",
            corner_radius=999,
            font=("Arial", 15, "bold"),
            height=40,
            command=lambda: app.top.Page(page.master).render()
        ).grid()
