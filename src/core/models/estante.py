"""Modelo de Estante do NeoLibro.

Define a classe Estante para gerenciamento
de obras em memória com operações CRUD.
"""
from typing import cast
from ..exceptions import DuplicateWorkError, MissingSearchCriteriaError
from . import HQ, Livro, Manga, Obra

class Estante:
    """Classe para gerenciamento de obras em memória.

    Armazena HQs, Livros e Mangás em coleções
    separadas e fornece operações CRUD.
    """
    def __init__(self) -> None:
        """Inicializa a estante com coleções vazias.

        Cria listas para HQs, Livros e Mangás,
        além de um contador para cada tipo.
        """
        self._hqs: list[HQ] = []
        self._livros: list[Livro] = []
        self._mangas: list[Manga] = []

        self._domain_map: dict[type[Obra], list[Obra]] = {
            HQ: cast(list[Obra], self._hqs),
            Livro: cast(list[Obra], self._livros),
            Manga: cast(list[Obra], self._mangas)
        }

    def _is_duplicate(self, obra: Obra) -> bool:
        """Verifica se a obra já existe na estante.

        Args:
            obra: Obra a ser verificada.

        Returns:
            True se a obra já existe, False caso contrário.

        Raises:
            DuplicateWorkError: Se a obra já estiver catalogada.
        """
        tipo = type(obra)
        colecao = self._domain_map[tipo]

        for duplicata in colecao:
            if obra.unique_dict() == duplicata.unique_dict():
                raise DuplicateWorkError(duplicata.titulo)

        return False

    def _gerar_codigo(self, tipo: type[Obra]) -> str:
        """Gera código único para a obra.

        Args:
            tipo: Tipo da obra (HQ, Livro ou Manga).

        Returns:
            Código gerado no formato PREFIXO-XXX.
        """
        numero: int = len(self._domain_map[tipo]) + 1
        prefixo: str = tipo.prefix

        codigo: str = f'{prefixo}-{numero:03d}'

        return codigo

    def _set_code(self, obra: Obra) -> None:
        """Define código para a obra se necessário.

        Gera e atribui código se a obra não tiver
        um código definido.

        Args:
            obra: Obra a receber o código.
        """
        if obra.codigo is None or obra.codigo == "":
            obra.codigo = self._gerar_codigo(type(obra))

    def _store(self, obra: Obra) -> None:
        """Armazena a obra na coleção apropriada.

        Adiciona a obra à lista correspondente
        baseado no seu tipo.

        Args:
            obra: Obra a ser armazenada.
        """
        self._domain_map[type(obra)].append(obra)

    def carregar(self, obras: list[Obra]) -> None:
        """Carrega obras na estante a partir de uma coleção existente.

        Args:
            obras: Lista de obras a serem carregadas.
        """
        for work in obras:
            self._store(work)

    def cadastrar(self, obra: Obra) -> Obra:
        """Adiciona uma obra à estante.
        Verifica duplicidade, gera código e
        armazena a obra na coleção apropriada.

        Args:
            obra: Obra a ser adicionada.

        Raises:
            DuplicateWorkError: Se a obra já tiver sido catalogada.
        """
        self._is_duplicate(obra)
        self._set_code(obra)
        self._store(obra)

        return obra

    def consultar(self, titulo: str|None=None, codigo: str|None=None) -> list[Obra]:
        """Busca obras por código ou título.

        Args:
            titulo: Título para busca (opcional).
            codigo: Código para busca (opcional).

        Returns:
            Lista de obras encontradas.
        """
        codigo_valido: bool = codigo is not None and codigo.strip() != ""
        titulo_valido: bool = titulo is not None and titulo.strip() != ""

        if not (codigo_valido or titulo_valido):
            raise MissingSearchCriteriaError()

        achados: list[Obra] = []
        for collection in self._domain_map.values():  #Custo: Temporal
            for obra in collection:
                if codigo and codigo == obra.codigo:
                    return [obra]

                elif titulo and titulo in obra.titulo:
                    achados.append(obra)

                # TODO: Future-> Verificar se ambos critérios foram passados

        return achados

    def ver_estante(self) -> list[Obra]:
        """Retorna todas as obras catalogadas na estante.

        Returns:
            Lista com todas as obras armazenadas.
        """
        return [
            work
                for collection in self._domain_map.values()
                    for work in collection
        ]

    def total_obras(self) -> int:
        """Retorna o total de obras na estante.

        Returns:
            Soma de todas as obras armazenadas.
        """
        return sum(len(lista) for lista in self._domain_map.values())
