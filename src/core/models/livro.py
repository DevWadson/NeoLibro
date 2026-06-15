"""Modelo de Livro do NeoLibro.

Define a classe Livro para livros tradicionais.
"""
from .obra import Obra

class Livro(Obra):
    """Classe representando um Livro tradicional.

    Herda de Obra e adiciona campos específicos:
        autor, editora, publicação e páginas.
    """
    prefix = "LVR"
    __fields__ = Obra.__fields__ + ["autor", "editora", "publicacao", "paginas"]

    def __init__(self,
                titulo: str,
                autor: str,
                editora: str,
                publicacao: int,
                paginas: int,
                preco: str,
                codigo: str|None = None
                ) -> None:
        """Inicializa um Livro com atributos específicos.

        Args:
            titulo: Nome do livro.
            autor: Autor do livro.
            editora: Editora do livro.
            publicacao: Ano de publicação.
            paginas: Número de páginas.
            preco: Preço do livro como string.
            codigo: Identificador único do livro.
        """
        super().__init__(titulo, preco, codigo)
        self.autor = autor
        self.editora = editora
        self.publicacao = publicacao
        self.paginas = paginas

    def __repr__(self) -> str:
        """Retorna representação formal para debug.

        Returns:
            str: Representação com todos os campos específicos do tipo.
        """
        return (
            f'{super().__repr__()}'
            f'autor={self.autor}\n'
            f'editora={self.editora}\n'
            f'publicacao={self.publicacao}\n'
            f'paginas={self.paginas})\n'
        )

    def __str__(self) -> str:
        """Retorna representação string de Livro.

        Returns:
            String com todos os campos específicos do tipo.
        """
        return (
            f'{super().__str__()}\n'
            f'{self.autor}\n'
            f'{self.editora}\n'
            f'{self.publicacao}\n'
            f'{self.paginas}\n'
        )
