import os

def limpiar_pantalla():
    """Limpia la consola para mejorar la legibilidad."""
    os.system('cls' if os.name == 'nt' else 'clear')