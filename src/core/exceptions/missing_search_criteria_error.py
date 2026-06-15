"""Exceção levantada quando nenhum critério de busca é fornecido."""
from .neolibro_error import NeoLibroError

class MissingSearchCriteriaError(NeoLibroError):
    """Exceção para buscas sem critério definido.

    Levantada quando consultar() é chamado sem título ou código.
    """
    def __init__(self) -> None:
        message: str = "Ao menos 1 critério precisa ser preenchido."
        super().__init__(message)
