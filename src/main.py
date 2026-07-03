"""Ponto de entrada da aplicação NeoLibro."""
from src.bootstrap import bootstrap
from src.gui import Window

def main():
    """Inicializa o bootstrap e inicia a interface gráfica."""
    nlservice = bootstrap()
    gui = Window(nlservice)
    gui.start()

if __name__ == "__main__":
    main()
