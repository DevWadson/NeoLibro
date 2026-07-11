"""Exceções de obra não encontrada do NeoLibro.

Define as exceções levantadas quando uma busca
por código ou título não encontra nenhuma obra.
"""
from .neolibro_error import NeoLibroError

class WorkNotFoundByCodeError(NeoLibroError):
    """Exceção levantada quando nenhuma obra é encontrada com o código informado."""
    def __init__(self, codigo: str) -> None:
        """Inicializa a exceção com o código buscado.

        Args:
            codigo: Código que não correspondeu a nenhuma obra.
        """
        message = f'{codigo}: Obra não encontrada!'
        super().__init__(message)

class WorkNotFoundByTitleError(NeoLibroError):
    """Exceção levantada quando o título informado é vazio ou nenhuma obra corresponde a ele."""
    def __init__(self, titulo: str) -> None:
        """Inicializa a exceção com o título buscado.

        Args:
            titulo: Título que não correspondeu a nenhuma obra, ou veio vazio.
        """
        message = f'{titulo}: Título não encontrado!'
        super().__init__(message)
