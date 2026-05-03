import customtkinter as ctk

class Pagina2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self, text="Página 2", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=20)