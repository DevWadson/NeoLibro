"""Serviço de aplicação do NeoLibro.

Orquestra a Estante e o Repository para coordenar
os casos de uso de cadastro e consulta de obras.
"""
from src.core import Estante, Obra, NeoLibroError, MissingSearchCriteriaError
from src.infra import ObraRepository

class NeoLibroService:
    """Serviço que gerencia obras do NeoLibro.

    Integra a estante (memória) com o repositório
    (banco de dados) para persistência e recuperação.
    """
    def __init__(self, estante: Estante, repo: ObraRepository) -> None:
        """Inicializa o serviço com estante e repositório.

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

    def consultar(self, codigo: str=None, titulo: str=None) -> Obra | list[Obra]:
        """Consulta obras na estante por código ou título.

        Delega a busca para a estante em memória, que é a
        fonte de verdade para operações de leitura.

        Args:
            codigo: Código da obra para busca exata (opcional).
            titulo: Título para busca parcial (opcional).

        Returns:
            A obra encontrada, se a busca for por código, ou a lista de
            obras encontradas, se a busca for por título.

        Raises:
            MissingSearchCriteriaError: Se nem código nem título forem informados.
            WorkNotFoundByCodeError: Se a busca por código não encontrar nenhuma obra.
            WorkNotFoundByTitleError: Se a busca por título não encontrar nenhuma obra.
        """
        codigo_valido: bool = codigo is not None and codigo.strip() != ""
        titulo_valido: bool = titulo is not None and titulo.strip() != ""

        if not (codigo_valido or titulo_valido):
            raise MissingSearchCriteriaError()

        if codigo:
            return self._estante.buscar_por_codigo(codigo=codigo)

        if titulo:
            return self._estante.buscar_por_titulo(titulo=titulo)
