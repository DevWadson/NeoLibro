"""Modelo SQLAlchemy de Mangá do NeoLibro.

Define a classe MangaModel para mapeamento
de mangás no banco de dados.
"""
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey
from .obra_model import ObraModel

class MangaModel(ObraModel):
    """Modelo SQLAlchemy para tabela de mangás.

    Herda de ObraModel e adiciona campos
    específicos de mangás com mapeamento
    polimórfico.
    """
    __tablename__ = "manga"
    __fields__ = ObraModel.__fields__ + ["autor", "editora", "publicacao", "capitulos"]
    __mapper_args__ = {"polymorphic_identity": "manga"}

    id = Column(INTEGER, ForeignKey("obra.id"), primary_key=True, index=True)
    autor = Column(VARCHAR(100), nullable=False)
    editora = Column(VARCHAR(80), nullable=False)
    publicacao = Column(INTEGER, nullable=False)
    capitulos = Column(INTEGER, nullable=False)
