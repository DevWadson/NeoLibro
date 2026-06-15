"""Modelo base de obra do NeoLibro.

Define a classe Obra como base para HQs, Livros e Mangás.
"""
from typing import Any
from decimal import Decimal, InvalidOperation
from ..exceptions import EmptyPriceError, InvalidTypePriceError, NegativePriceError

class Obra:
    """Classe base para todas as obras do NeoLibro.

    Define atributos comuns e métodos utilitários
    para serialização e conversão de dados.
    """
    prefix: str
    __fields__ = ["codigo", "titulo", "preco"]
    __unique_fields__ = list(set(__fields__) - {"codigo"})

    def __init__(self, titulo: str, preco: str, codigo: str|None=None) -> None:
        """Inicializa uma obra com código, título e preço.

        Args:
            titulo: Nome da obra.
            preco: Preço da obra como string (convertido para Decimal internamente).
            codigo: Identificador único da obra.
        """
        self.codigo = codigo
        self.titulo = titulo
        self.preco = self._parse_preco(preco)

    def __repr__(self) -> str:
        """Retorna representação formal da obra para debug.

        Returns:
            str: Representação com prefixo, código, título e preço.
        """
        return (
            f'{self.prefix}(\n'
            f'codigo={self.codigo}\n'
            f'titulo={self.titulo}\n'
            f'preco={self.preco}\n'
        )

    def __str__(self) -> str:
        """Retorna representação string da obra.

        Returns:
            String com título e código da obra.
        """
        return (
            f'{self.titulo}\n'
            f'{self.codigo}\n'
        )

    def _parse_preco(self, preco: str) -> Decimal:
        """Converte preço para Decimal.

        Args:
            preco: Valor a ser convertido.

        Returns:
            Decimal: Valor convertido para Decimal.
        """
        if isinstance(preco, str) and preco.strip() == "":
            raise EmptyPriceError()

        try:
            valor: Decimal = preco if isinstance(preco, Decimal) else Decimal(preco)

        except (InvalidOperation, ValueError, TypeError):
            raise InvalidTypePriceError(preco) from None

        if Decimal(valor) < 0:
            raise NegativePriceError(preco)

        return valor

    def serialized(self) -> dict[str, Any]:
        """Serializa a obra para dicionário.

        Returns:
            Dicionário com os campos da obra.
        """
        return {
            campo: getattr(self, campo, None)
            for campo in self.__fields__
        }

    def unique_dict(self) -> dict[str, Any]:
        """Retorna dicionário para comparação de duplicidade.

        Exclui o campo 'codigo' da comparação, permitindo identificar
        obras duplicadas mesmo com códigos diferentes.

        Returns:
            dict[str, Any]: Dicionário com campos comparáveis da obra.
        """
        return {
            campo: getattr(self, campo, None)
            for campo in self.__unique_fields__
        }
