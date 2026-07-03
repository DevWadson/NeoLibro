"""Frame lateral de navegação do NeoLibro.

Contém os botões de acesso às funcionalidades da aplicação.
"""
from customtkinter import CTkFrame

class MenuArea(CTkFrame):
    """Frame lateral que agrupa os botões do menu de navegação."""
    def __init__(self, parent, **kwargs) -> None:
        """Inicializa o frame lateral de navegação.

        Args:
            parent: Widget pai ao qual o frame será anexado.
        """
        super().__init__(master=parent, **kwargs)
