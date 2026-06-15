"""Modelo de Manga do NeoLibro.

Define a classe Manga para mangás japoneses.
"""
from .obra import Obra

class Manga(Obra):
    """Classe representando um Manga japonês.

    Herda de Obra e adiciona campos específicos:
    autor, editora, publicação e capítulos.
    """
    prefix = "MNG"
    __fields__ = Obra.__fields__ + ["autor", "editora", "publicacao", "capitulos"]

    def __init__(self,
                titulo: str,
                autor: str,
                editora: str,
                publicacao: int,
                capitulos: int,
                preco: str,
                codigo: str | None = None
                ) -> None:
        """Inicializa um Mangá com atributos específicos.

        Args:
            titulo: Nome do mangá.
            autor: Autor do mangá.
            editora: Editora do mangá.
            publicacao: Ano de publicação.
            capitulos: Número de capítulos.
            preco: Preço do mangá como string.
            codigo: Identificador único do mangá.
        """
        super().__init__(titulo, preco, codigo)
        self.autor = autor
        self.editora = editora
        self.publicacao = publicacao
        self.capitulos = capitulos

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
            f'capitulos={self.capitulos})\n'
        )

    def __str__(self) -> str:
        """Retorna representação string do Mangá.

        Returns:
            String com todos os campos específicos do tipo.
        """
        return (
            f'{super().__str__()}\n'
            f'{self.autor}\n'
            f'{self.editora}\n'
            f'{self.publicacao}\n'
            f'{self.capitulos}\n'
        )
