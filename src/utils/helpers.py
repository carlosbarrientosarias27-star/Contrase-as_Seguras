import os
import subprocess

def limpiar_pantalla(sistema=None):
    """
    Limpia la consola. 
    Usa el parámetro 'sistema' para evitar mockear os.name en los tests.
    """
    # Si no se pasa un sistema, usamos el real del entorno
    nombre_os = sistema if sistema is not None else os.name
    
    # Usamos listas para subprocess.run, lo cual es seguro según Bandit
    comando = ['cls'] if nombre_os == 'nt' else ['clear']
    
    try:
        subprocess.run(comando, check=True)
    except Exception:
        # Silenciamos errores si el comando no existe en el entorno
        pass