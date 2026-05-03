import customtkinter as ctk
from Pages.Home import Home
from Pages.Pagina2 import Pagina2
from Components.Sidebar import Sidebar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Organização Escola")
        self.geometry("1080x920")
        self.minsize(400, 180)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew")

        self.pagina_atual = None

        pages = {
            "Home":    self.mostrar_home,
            "Página 2": self.mostrar_pagina2,
        }

        sidebar = Sidebar(self, pages)
        sidebar.grid(row=0, column=0, sticky="ns")

    def _trocar(self, nova_pagina):
        if self.pagina_atual:
            self.pagina_atual.destroy()
        self.pagina_atual = nova_pagina(self.container)
        self.pagina_atual.pack(fill="both", expand=True)

    def mostrar_home(self):
        self._trocar(Home)

    def mostrar_pagina2(self):
        self._trocar(Pagina2)

if __name__ == "__main__":
    App().mainloop()