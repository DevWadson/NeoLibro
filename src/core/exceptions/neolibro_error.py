"""Exceção base do NeoLibro.

Define a classe raiz para todas as exceções customizadas
do domínio NeoLibro.
"""

class NeoLibroError(Exception):
    """Exceção base para erros do NeoLibro.

    Todas as exceções específicas do domínio devem herdar
    desta classe para permitir captura genérica.
    """
    pass
