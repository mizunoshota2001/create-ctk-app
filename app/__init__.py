import customtkinter as ctk
from app import top

master = ctk.CTk()
master.title("CreateCTkApp")
master.geometry("500x300")
top.Page(master).render()

def start():
    master.mainloop()
