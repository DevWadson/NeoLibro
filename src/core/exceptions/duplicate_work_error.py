"""Exceção levantada ao tentar adicionar obra duplicada."""
from .neolibro_error import NeoLibroError

class DuplicateWorkError(NeoLibroError):
    """Exceção para obras já catalogadas na estante.
    Levantada quando se tenta adicionar uma obra que já
    existe na estante, baseada na comparação de campos.
    """
    def __init__(self, titulo: str) -> None:
        """Inicializa a exceção com o título da obra duplicada.

        Args:
            titulo: Título da obra que já está catalogada.
        """
        message = (
            f'A obra {titulo} já está catalogada.'
        )
        super().__init__(message)
