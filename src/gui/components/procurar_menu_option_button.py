"""Botão de menu para acesso à procura de obras."""
from customtkinter import CTkButton

class ProcurarMenuOptionButton(CTkButton):
    """Botão do menu que aciona a tela de procura de obras."""
    def __init__(self, parent, main_area, **kwargs) -> None:
        """Inicializa o botão com referência à MainArea.

        Args:
            parent: Widget pai ao qual o botão será anexado.
            main_area: Instância de MainArea a ser notificada ao clicar.
        """
        super().__init__(parent, text="Procurar", **kwargs)
        self.main_area = main_area
        self.configure(command=self._on_click)

    def _on_click(self):
        """Notifica a MainArea para exibir as opções de procura."""
        self.main_area.mostrar_opcoes_procura()
