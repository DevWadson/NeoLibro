"""Módulo de banco de dados do NeoLibro.

Expõe modelos SQLAlchemy e a inicialização da conexão.
"""
from .models import HqModel, LivroModel, MangaModel, ObraModel
from .connection import setup_database
