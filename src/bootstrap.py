"""Bootstrap do NeoLibro.

Responsável por montar e conectar as dependências
da aplicação antes da inicialização da interface.
"""
from src.application import NeoLibroService
from dotenv import load_dotenv
from src.core import Estante
from src.infra import setup_database, ObraRepository

load_dotenv()

def bootstrap() -> NeoLibroService:
    """Monta e retorna o serviço de aplicação configurado.

    Inicializa o banco de dados, instancia o repositório,
    a estante e o serviço, retornando-o pronto para uso.
    """
    session = setup_database()
    repo = ObraRepository(session)
    shelf = Estante()
    nlservice = NeoLibroService(shelf, repo)

    return nlservice
