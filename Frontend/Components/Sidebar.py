import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, pages: dict, **kwargs):
        super().__init__(master, width=180, corner_radius=0, **kwargs)
        self.pack_propagate(False)

        self.pages = pages
        self.buttons = {}
        self.active = None

        for name, command in pages.items():
            btn = ctk.CTkButton(
                self,
                text=name,
                anchor="w",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray85", "gray25"),
                corner_radius=8,
                command=lambda n=name, c=command: self._selecionar(n, c),
            )
            btn.pack(pady=(20 if not self.buttons else 4), padx=12, fill="x")
            self.buttons[name] = btn

        first_name, first_cmd = next(iter(pages.items()))
        self._selecionar(first_name, first_cmd)

    def _selecionar(self, name, command):
        if self.active:
            self.buttons[self.active].configure(fg_color="transparent")
        self.buttons[name].configure(fg_color=("gray75", "gray30"))
        self.active = name
        command()