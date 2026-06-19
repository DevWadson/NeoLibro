"""Modelo SQLAlchemy de obra do NeoLibro.

Define a classe ObraModel para mapeamento
de obras no banco de dados.
"""
from typing import Any
from sqlalchemy import DECIMAL, INTEGER, VARCHAR, Column
from ..base import Base

class ObraModel(Base):
    """Modelo SQLAlchemy para tabela de obras.

    Define estrutura base para mapeamento
    polimórfico de HQs, Livros e Mangás.
    """
    __tablename__ = "obra"
    __fields__ = ["codigo", "titulo", "preco"]
    __unique_fields__ = list(set(__fields__) - {"codigo"})
    tipo_obra = Column(VARCHAR(12))

    __mapper_args__ = {
        "polymorphic_on": tipo_obra,
        "polymorphic_identity": "obra"
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True, index=True)
    codigo = Column(VARCHAR(7), nullable=False, unique=True)
    titulo = Column(VARCHAR(150), nullable=False, unique=False)
    preco = Column(DECIMAL(10, 2), nullable=False, unique=False)

    def serialized_model(self) -> dict[str, Any]:
        """Serializa o model para reconstrução do domínio.

        Returns:
            Dicionário com os campos definidos em __fields__.
        """
        return {
            campo: getattr(self, campo, None)
            for campo in self.__fields__
        }

    def unique_model(self) -> dict[str, Any]:
        """Retorna campos usados para checagem de duplicidade.

        Returns:
            Dicionário com os campos definidos em __unique_fields__.
        """
        return {
            campo: getattr(self, campo, None)
            for campo in self.__unique_fields__
        }
