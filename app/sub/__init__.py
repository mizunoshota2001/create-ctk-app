import customtkinter as ctk
from app import top


class Page:
    def __init__(self, master: ctk.CTk):
        self.master = master

    def render(self):
        frame = ctk.CTkFrame(self.master)
        frame.pack(fill="both", expand=True)
        label = ctk.CTkLabel(frame, text="subパッケージのPageクラスです")
        label.pack(pady=10)
        switch_button = ctk.CTkButton(
            frame, text="フレームを切り替え", command=lambda: self.replace(top.Page(self.master)))
        switch_button.pack(pady=10)

    def replace(self, page: "Page"):
        [child.destroy() for child in self.master.winfo_children()]
        page.render()
