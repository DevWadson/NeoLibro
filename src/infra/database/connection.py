"""Módulo de conexão com banco de dados do NeoLibro.

Resolve a URL de banco ativa e fornece a inicialização
completa da engine, tabelas e sessão SQLAlchemy.
"""
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker
from .base import Base
from src.config import get_active_database_url

def _get_engine(conn_url: str) -> Engine:
    """Cria a engine de conexão com o banco de dados.

    Args:
        conn_url: URL de conexão com o banco de dados.

    Returns:
        Engine SQLAlchemy configurada para o banco de dados.
    """
    return create_engine(conn_url, echo=False)

def _create_tables(engine: Engine) -> None:
    """Cria as tabelas do banco a partir dos modelos registrados.

    Args:
        engine: Engine SQLAlchemy configurada.
    """
    Base.metadata.create_all(bind=engine)

def _create_session_factory(engine: Engine) -> sessionmaker:
    """Cria a fábrica de sessões SQLAlchemy.

    Args:
        engine: Engine SQLAlchemy configurada.

    Returns:
        Sessionmaker para criar sessões vinculadas à engine.
    """
    return sessionmaker(bind=engine)

def setup_database() -> Session:
    """Inicializa a conexão com o banco e retorna uma sessão ativa.

    Resolve a URL de banco ativa, cria a engine, garante a criação
    das tabelas e gera uma sessão pronta para uso.

    Returns:
        Sessão SQLAlchemy ativa, vinculada à engine inicializada.
    """
    url = get_active_database_url()
    engine = _get_engine(url)
    _create_tables(engine)
    session_factory = _create_session_factory(engine)

    return session_factory()
