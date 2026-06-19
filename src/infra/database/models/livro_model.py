"""Modelo SQLAlchemy de Livro do NeoLibro.

Define a classe LivroModel para mapeamento
de livros no banco de dados.
"""
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey
from .obra_model import ObraModel

class LivroModel(ObraModel):
    """Modelo SQLAlchemy para tabela de livros.

    Herda de ObraModel e adiciona campos
    específicos de livros com mapeamento
    polimórfico.
    """
    __tablename__ = "livro"
    __fields__ = ObraModel.__fields__ + ["autor", "editora", "publicacao", "paginas"]
    __mapper_args__ = {"polymorphic_identity": "livro"}

    id = Column(INTEGER, ForeignKey("obra.id"), primary_key=True, index=True)
    autor = Column(VARCHAR(100), nullable=False)
    editora = Column(VARCHAR(80), nullable=False)
    publicacao = Column(INTEGER, nullable=False)
    paginas = Column(INTEGER, nullable=False)
