"""Formulário de cadastro de Livro do NeoLibro."""
from customtkinter import CTkButton, CTkEntry, CTkFrame
from src.core import Livro

class LivroForm(CTkFrame):
    """Formulário para coleta dos dados de cadastro de um Livro."""
    def __init__(self, parent, on_submit, **kwargs) -> None:
        """Inicializa o formulário com o callback de submissão.

        Args:
            parent: Widget pai ao qual o formulário será anexado.
            on_submit: Função chamada com o Livro montado ao salvar.
        """
        super().__init__(parent, **kwargs)
        self._on_submit = on_submit
        self._render_form()
        self.save = CTkButton(self, text="Salvar", command=self._salvar).pack(padx=10, pady=5)

    def _render_form(self) -> None:
        """Renderiza os campos de entrada correspondentes ao Livro."""
        self.titulo = CTkEntry(self, placeholder_text="Título")
        self.autor = CTkEntry(self, placeholder_text="Autor")
        self.editora = CTkEntry(self, placeholder_text="Editora")
        self.publicacao = CTkEntry(self, placeholder_text="Publicação")
        self.paginas = CTkEntry(self, placeholder_text="Páginas")
        self.preco = CTkEntry(self, placeholder_text="Preço")

        self.titulo.pack()
        self.autor.pack()
        self.editora.pack()
        self.publicacao.pack()
        self.paginas.pack()
        self.preco.pack()

    def _extract_data(self) -> Livro:
        """Monta um Livro a partir dos valores preenchidos nos campos.

        Returns:
            O Livro montado com os dados do formulário.
        """
        return Livro(
            titulo=self.titulo.get(),
            autor=self.autor.get(),
            editora=self.editora.get(),
            publicacao=int(self.publicacao.get()),
            paginas=int(self.paginas.get()),
            preco=self.preco.get()
        )

    def _salvar(self) -> None:
        """Extrai os dados preenchidos e os entrega ao callback de submissão."""
        dados = self._extract_data()
        self._on_submit(dados)
