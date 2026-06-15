"""Modelo de HQ do NeoLibro.

Define a classe HQ para histórias em quadrinhos.
"""
from .obra import Obra

class HQ(Obra):
    """Classe representando uma História em Quadrinhos.

    Herda de Obra e adiciona campos específicos:
    indústria, edição e volume.
    """
    prefix = "HQ"
    __fields__ = Obra.__fields__ + ["industria", "edicao", "volume"]

    def __init__(self,
                titulo: str,
                industria: str,
                edicao: int,
                volume: int,
                preco: str,
                codigo: str | None = None
                ) -> None:
        """Inicializa uma HQ com atributos específicos.

        Args:
            titulo: Nome da HQ.
            industria: Editora/indústria da HQ.
            edicao: Número da edição.
            volume: Número do volume.
            preco: Preço da HQ como string.
            codigo: Identificador único da HQ.
        """
        super().__init__(titulo, preco, codigo)
        self.industria = industria
        self.edicao = edicao
        self.volume = volume

    def __repr__(self) -> str:
        """Retorna representação formal para debug.

        Returns:
            str: Representação com todos os campos específicos do tipo.
        """
        return (
            f'{super().__repr__()}'
            f'industria={self.industria}\n'
            f'edicao={self.edicao}\n'
            f'volume={self.volume})\n'
        )

    def __str__(self) -> str:
        """Retorna representação string da HQ.

        Returns:
            String com todos os campos específicos do tipo.
        """
        return (
            f'{super().__str__()}\n'
            f'{self.industria}\n'
            f'{self.edicao}\n'
            f'{self.volume}\n'
        )
