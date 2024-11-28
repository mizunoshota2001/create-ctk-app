import customtkinter as ctk
from app import top

FONT_TYPE = "meiryo"
master = ctk.CTk()
master.title("カスタムTkinterアプリ")
master.geometry("500x500")
top.Page(master).render()

def start():
    master.mainloop()
