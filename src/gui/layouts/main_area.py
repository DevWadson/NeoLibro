"""Frame principal de conteúdo do NeoLibro.

Responsável por exibir e alternar o conteúdo dinâmico
da interface conforme as ações do menu.
"""
from customtkinter import CTkButton, CTkEntry, CTkFrame
from src.application import NeoLibroService
from src.core import HQ, Livro, Manga, Obra
from ..forms import HQForm, LivroForm, MangaForm

class MainArea(CTkFrame):
    """Frame principal que gerencia o conteúdo dinâmico da interface.

    Constrói e exibe os estados da aplicação: opções de cadastro,
    formulário de procura e demais telas acionadas pelo menu.
    """
    def __init__(self, parent, nlservice: NeoLibroService, **kwargs) -> None:
        """Inicializa o frame principal com o serviço de aplicação.

        Args:
            parent: Widget pai ao qual o frame será anexado.
            nlservice: Instância do serviço de aplicação.
        """
        super().__init__(master=parent, **kwargs)
        self._available_map: dict[type[Obra], type[CTkFrame]] = {
            HQ: HQForm,
            Livro: LivroForm,
            Manga: MangaForm
        }
        self._nlservice = nlservice

    def _show_form(self, form) -> None:
        """Renderiza o formulário correspondente ao tipo selecionado.

        Args:
            form: Classe do formulário a ser instanciada e exibida.
        """
        form(self, on_submit=self.cadastrar).pack(fill="both", expand=True)

    def mostrar_opcoes_cadastro(self) -> None:
        """Exibe os botões de seleção de tipo para cadastro de obra."""
        for _Available_type, forms in self._available_map.items():
            CTkButton(self,
                text=_Available_type.__name__,
                command=lambda form=forms:self._show_form(form)
            ).pack(padx=10, pady=5)

    def mostrar_opcoes_procura(self) -> None:
        """Exibe os campos de busca e o botão de procura."""
        codigo = CTkEntry(self, placeholder_text="Código")
        titulo = CTkEntry(self, placeholder_text="Título")
        codigo.pack()
        titulo.pack()

        CTkButton(self, text="Buscar", command=None).pack(padx=10, pady=5)

    def cadastrar(self, obra: Obra):
        """Encaminha a obra montada pelo formulário para cadastro.

        Args:
            obra: Obra já construída pelo formulário, pronta para persistência.
        """
        self._nlservice.cadastrar(obra)
