"""Repositório de obras do NeoLibro.

Define a classe ObraRepository para persistência
de obras em banco de dados.
"""
from sqlalchemy.orm import Session
from src.infra.database import HqModel, LivroModel, MangaModel, ObraModel
from src.core.models import HQ, Livro, Manga, Obra

class ObraRepository:
    """Repositório para operações CRUD de obras.

    Fornece métodos para salvar, buscar e exibir
    obras no banco de dados.
    """
    def __init__(self, session: Session) -> None:
        self._session = session
        self._domain_map = {
            HqModel: HQ,
            LivroModel: Livro,
            MangaModel: Manga
        }
        self._model_map = {
            HQ: HqModel,
            Livro: LivroModel,
            Manga: MangaModel
        }

    def _get_model(self, obra: Obra) -> type[ObraModel]:
        """Retorna o modelo SQLAlchemy correspondente.

        Mapeia o tipo de obra (HQ, Livro, Mangá)
        para o modelo de banco de dados adequado.
        """
        typo = type(obra)
        return self._model_map[typo]

    def _get_domain(self, obra: ObraModel) -> type[Obra]:
        """Retorna a classe de domínio correspondente ao model.

        Mapeia o tipo de model (HqModel, LivroModel, MangaModel)
        para a classe de domínio adequada.
        """
        typo = type(obra)
        return self._domain_map[typo]

    def _to_model(self, obra: Obra) -> ObraModel:
        """Converte obra para modelo de banco de dados.

        Transforma o objeto de domínio em instância
        do modelo SQLAlchemy para persistência.
        """
        ModelClass = self._get_model(obra)
        work_data = obra.serialized()

        return ModelClass(**work_data)

    def _to_domain(self, obra: ObraModel) -> Obra:
        """Converte model de banco de dados para obra de domínio.

        Transforma a instância do modelo SQLAlchemy em
        objeto de domínio reconstruído a partir dos dados persistidos.
        """
        DomainClass = self._get_domain(obra)
        model_data = obra.serialized_model()

        return DomainClass(**model_data)

    def _is_duplicate(self, obra: ObraModel) -> bool:
        """Verifica duplicidade da obra no banco (defesa em profundidade).

        A validação principal ocorre na Estante; este método garante
        que nenhuma obra duplicada seja persistida em nenhuma circunstância.

        Raises:
            ValueError: Se já existir obra com os mesmos campos únicos.
        """
        Model = type(obra)
        filters = {
            field: getattr(obra, field, None)
            for field in Model.__unique_fields__
        }

        candidates = self._session.query(Model).filter_by(**filters).first()
        if candidates:
            raise ValueError ("Duplicado, brother!") # TODO: Future->Lançar Excessão apropriada

        return False

    def carregar_obras(self) -> list[Obra]:
        """Carrega todas as obras do banco para hidratação da Estante.

        Returns:
            Lista de obras de domínio reconstruídas a partir do banco.
        """
        all_works = self._session.query(ObraModel).all()

        return [
            self._to_domain(work)
            for work in all_works
        ] # Custo: Temporal

    def salvar(self, obra: Obra) -> Obra:
        """Persiste uma nova obra no banco de dados.

        Converte a obra de domínio em model, verifica duplicidade
        como defesa em profundidade e persiste no banco.

        Args:
            obra: Obra de domínio já validada e com código definido pela Estante.

        Returns:
            Obra de domínio reconstruída a partir do model persistido.
        """
        new_work: ObraModel = self._to_model(obra)

        self._is_duplicate(new_work)
        self._session.add(new_work)
        self._session.flush()
        self._session.commit()
        self._session.refresh(new_work)

        return self._to_domain(new_work)
