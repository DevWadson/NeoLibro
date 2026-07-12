"""Formulário de cadastro de Mangá do NeoLibro."""
from customtkinter import CTkButton, CTkEntry, CTkFrame
from src.core import Manga

class MangaForm(CTkFrame):
    """Formulário para coleta dos dados de cadastro de um Mangá."""
    def __init__(self, parent, on_submit, **kwargs) -> None:
        """Inicializa o formulário com o callback de submissão.

        Args:
            parent: Widget pai ao qual o formulário será anexado.
            on_submit: Função chamada com o Mangá montado ao salvar.
        """
        super().__init__(parent, **kwargs)
        self._on_submit = on_submit
        self._render_form()
        self.save = CTkButton(self, text="Salvar", command=self._salvar).pack(padx=10, pady=5)

    def _render_form(self) -> None:
        """Renderiza os campos de entrada correspondentes ao Mangá."""
        self.titulo = CTkEntry(self, placeholder_text="Título")
        self.autor = CTkEntry(self, placeholder_text="Autor")
        self.editora = CTkEntry(self, placeholder_text="Editora")
        self.publicacao = CTkEntry(self, placeholder_text="Publicação")
        self.capitulos = CTkEntry(self, placeholder_text="Capítulos")
        self.preco = CTkEntry(self, placeholder_text="Preço")

        self.titulo.pack()
        self.autor.pack()
        self.editora.pack()
        self.publicacao.pack()
        self.capitulos.pack()
        self.preco.pack()

    def _extract_data(self) -> Manga:
        """Monta um Mangá a partir dos valores preenchidos nos campos.

        Returns:
            O Mangá montado com os dados do formulário.
        """
        return Manga(
            titulo=self.titulo.get(),
            autor=self.autor.get(),
            editora=self.editora.get(),
            publicacao=int(self.publicacao.get()),
            capitulos=int(self.capitulos.get()),
            preco=self.preco.get()
        )

    def _salvar(self) -> None:
        """Extrai os dados preenchidos e os entrega ao callback de submissão."""
        dados = self._extract_data()
        self._on_submit(dados)
