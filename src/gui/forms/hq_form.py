"""Formulário de cadastro de HQ do NeoLibro."""
from customtkinter import CTkButton, CTkEntry, CTkFrame
from src.core import HQ

class HQForm(CTkFrame):
    """Formulário para coleta dos dados de cadastro de uma HQ."""
    def __init__(self, parent, on_submit, **kwargs) -> None:
        """Inicializa o formulário com o callback de submissão.

        Args:
            parent: Widget pai ao qual o formulário será anexado.
            on_submit: Função chamada com a HQ montada ao salvar.
        """
        super().__init__(parent, **kwargs)
        self._on_submit = on_submit
        self._render_form()
        self.save = CTkButton(self, text="Salvar", command=self._salvar).pack(padx=10, pady=5)

    def _render_form(self) -> None:
        """Renderiza os campos de entrada correspondentes à HQ."""
        self.titulo = CTkEntry(self, placeholder_text="Título")
        self.industria = CTkEntry(self, placeholder_text="Indústria")
        self.edicao = CTkEntry(self, placeholder_text="Edição")
        self.volume = CTkEntry(self, placeholder_text="Volume")
        self.preco = CTkEntry(self, placeholder_text="Preço")

        self.titulo.pack()
        self.industria.pack()
        self.edicao.pack()
        self.volume.pack()
        self.preco.pack()

    def _extract_data(self) -> HQ:
        """Monta uma HQ a partir dos valores preenchidos nos campos.

        Returns:
            A HQ montada com os dados do formulário.
        """
        return HQ(
            titulo=self.titulo.get(),
            industria=self.industria.get(),
            edicao=int(self.edicao.get()),
            volume=int(self.volume.get()),
            preco=self.preco.get()
        )

    def _salvar(self) -> None:
        """Extrai os dados preenchidos e os entrega ao callback de submissão."""
        dados = self._extract_data()
        self._on_submit(dados)
