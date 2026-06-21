"""Módulo de infraestrutura do NeoLibro.

Expõe a inicialização da conexão com o banco de dados
e o repositório de obras.
"""
from .database import setup_database
from .repository import ObraRepository
