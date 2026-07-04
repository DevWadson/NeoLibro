"""Serviço de aplicação do NeoLibro.

Orquestra a Estante e o Repository para coordenar
os casos de uso de cadastro e consulta de obras.
"""
from src.core import Estante, Obra, NeoLibroError
from src.infra import ObraRepository

class NeoLibroService:
    """Serviço que gerencia obras do NeoLibro.

    Integra a estante (memória) com o repositório
    (banco de dados) para persistência e recuperação.
    """
    def __init__(self, estante: Estante, repo: ObraRepository) -> None:
        """Inicializa o serviço com estante e repositório.

        Configura o mapeamento entre modelos de domínio
        e modelos de banco de dados.

        Args:
            estante: Instância de Estante para gerenciamento
            em memória das obras.

            repo: Instância de ObraRepository para persistência
            em banco de dados.
        """
        self._estante = estante
        self._repo = repo

    def cadastrar(self, obra: Obra) -> None:
        """Cadastra uma obra na estante e persiste no banco.

        Adiciona a obra à estante em memória e, em seguida,
        salva no repositório. Se a persistência falhar, a obra
        permanece na estante para não perder o cadastro do usuário.

        Args:
            obra: Obra a ser cadastrada.

        Raises:
            NeoLibroError: Se ocorrer falha ao persistir a obra.
        """
        try:
            self._estante.cadastrar(obra)
            self._repo.salvar(obra)

        except (NeoLibroError, ValueError, TypeError) as exc:
            raise NeoLibroError(f'Erro ao cadastrar obra "{obra.titulo}"') from exc

    def consultar(self, codigo: str=None, titulo: str=None) -> list[Obra]:
        """Consulta obras na estante por código ou título.

        Delega a busca para a estante em memória, que é a
        fonte de verdade para operações de leitura.

        Args:
            codigo: Código da obra para busca exata (opcional).
            titulo: Título para busca parcial (opcional).

        Returns:
            Lista de obras encontradas.
        """
        if codigo:
            return self._estante.consultar(codigo=codigo)
        if titulo:
            return self._estante.consultar(titulo=titulo)
