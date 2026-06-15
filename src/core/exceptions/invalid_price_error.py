"""Exceção relacionadas a preço no NeoLibro."""
from .neolibro_error import NeoLibroError

class InvalidTypePriceError(NeoLibroError):
    """Exceção lançada quando o tipo do preço é inválido."""
    def __init__(self, preco: object) -> None:
        """Inicializa a exceção com o preço fornecido.

        Args:
            preco: Valor recebido por preço.
        """
        message = f'{type(preco).__name__} é um tipo inválido para preço.'
        super().__init__(message)

class EmptyPriceError(NeoLibroError):
    """Exceção lançada quando o preço está vazio."""
    def __init__(self) -> None:
        message = "Preço não pode ser vazio."
        super().__init__(message)

class NegativePriceError(NeoLibroError):
    """Exceção lançada quando o preço é negativo."""
    def __init__(self, preco) -> None:
        """Inicializa a exceção com o preço fornecido.

        Args:
            preco: Valor recebido por preço.
        """
        message = f'{preco}: Preço não pode ser menor que 0.'
        super().__init__(message)
