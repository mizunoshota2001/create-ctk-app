import customtkinter as ctk
import app.top

master = ctk.CTk()
master.title("CreateCTkApp")
master.geometry("500x300")
app.top.Page(master).render()

def start():
    master.mainloop()
