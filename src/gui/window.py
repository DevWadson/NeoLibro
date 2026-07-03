"""Janela principal do NeoLibro.

Define a estrutura da interface e coordena layouts e componentes.
"""
from customtkinter import CTk
from src.application import NeoLibroService
from src.gui.components import CadastrarMenuOptionButton, ProcurarMenuOptionButton
from src.gui.layouts import MainArea, MenuArea

class Window(CTk):
    """Janela principal da aplicação NeoLibro.

    Inicializa os layouts e os botões do menu, coordenando
    a comunicação entre MenuArea e MainArea.
    """
    def __init__(self, nlservice: NeoLibroService):
        """Inicializa a janela com layouts e botões do menu.

        Args:
            nlservice: Instância do serviço de aplicação,
            repassada para a MainArea.
        """
        super().__init__()
        self._nlservice = nlservice
        self.title("NeoLibro")
        self.geometry("1000x600")

        # Layouts
        self.main_area = MainArea(parent=self, nlservice=self._nlservice)
        self.menu_area = MenuArea(parent=self)

        self.main_area.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)
        self.menu_area.grid(row=0, column=0, sticky="ns")
        self.grid_columnconfigure(0, minsize=200)

        # Botões
        cadastrar_button_option = CadastrarMenuOptionButton(self.menu_area, self.main_area)
        procurar_button_option = ProcurarMenuOptionButton(self.menu_area, self.main_area)
        cadastrar_button_option.pack(padx=10, pady=5)
        procurar_button_option.pack(padx=10, pady=5)

    def start(self) -> None:
        """Inicia o loop principal da interface."""
        return self.mainloop()
