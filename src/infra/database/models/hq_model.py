"""Modelo SQLAlchemy de HQ do NeoLibro.

Define a classe HqModel para mapeamento
de histórias em quadrinhos no banco de dados.
"""
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey
from .obra_model import ObraModel

class HqModel(ObraModel):
    """Modelo SQLAlchemy para tabela de HQs.

    Herda de ObraModel e adiciona campos
    específicos de histórias em quadrinhos
    com mapeamento polimórfico.
    """
    __tablename__ = "hq"
    __fields__ = ObraModel.__fields__ + ["industria", "edicao", "volume"]
    __mapper_args__ = {"polymorphic_identity": "hq"}

    id = Column(INTEGER, ForeignKey("obra.id"), primary_key=True, index=True)
    industria = Column(VARCHAR(60), nullable=False)
    edicao = Column(INTEGER, nullable=False)
    volume = Column(INTEGER, nullable=False)
