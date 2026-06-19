"""Base declarativa para modelos SQLAlchemy do NeoLibro."""
from sqlalchemy import Engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_tables(engine: Engine) -> None:
    """Cria todas as tabelas no banco SQLite.

    Utiliza os modelos SQLAlchemy registrados
    para criar as tabelas necessárias no banco.
    """
    return Base.metadata.create_all(bind=engine)
