import os
import subprocess

def limpiar_pantalla():
    """Limpia la consola usando subprocess para evitar vulnerabilidades de shell."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['cls'], check=True)
        else:  # macOS/Linux
            subprocess.run(['clear'], check=True)
    except Exception:
        # Fallback if the command fails in certain environments
        pass