import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self, text="Home", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)