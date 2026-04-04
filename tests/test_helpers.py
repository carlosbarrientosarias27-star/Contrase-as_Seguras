import pytest
import subprocess
from src.utils.helpers import limpiar_pantalla


# --- Casos Normales (N) ---

def test_limpiar_pantalla_ejecuta_comando_windows(monkeypatch):
    """Verifica que se llame a 'cls' inyectando el sistema 'nt'."""
    captura = []
    
    # Mockeamos subprocess.run en lugar de os.system
    def mock_run(comando, **kwargs):
        captura.append(comando[0])

    monkeypatch.setattr(subprocess, "run", mock_run)

    # Act: Inyectamos el nombre del sistema directamente
    limpiar_pantalla(sistema="nt")

    # Assert
    assert "cls" in captura

def test_limpiar_pantalla_ejecuta_comando_unix(monkeypatch):
    """Verifica que se llame a 'clear' inyectando un sistema posix."""
    captura = []
    
    def mock_run(comando, **kwargs):
        captura.append(comando[0])

    monkeypatch.setattr(subprocess, "run", mock_run)

    # Act
    limpiar_pantalla(sistema="posix")

    # Assert
    assert "clear" in captura

# --- Casos Límite (L) ---

def test_limpiar_pantalla_nombre_os_vacio(monkeypatch):
    """
    Verifica el comportamiento cuando os.name es una cadena vacía (debe usar 'clear' por el else).
    """
    # Arrange
    comando_ejecutado = None
    monkeypatch.setattr(os, "name", "")
    monkeypatch.setattr(os, "system", lambda cmd: setattr(pytest, "cmd_tmp", cmd))

    # Act
    limpiar_pantalla()

    # Assert
    assert pytest.cmd_tmp == "clear"

# --- Casos de Error / Edge (E) ---

def test_limpiar_pantalla_error_en_llamada_sistema(monkeypatch):
    """
    Verifica que una excepción en os.system se propague correctamente si el sistema falla.
    """
    # Arrange
    def mock_system_error(comando):
        raise OSError("Fallo del sistema")

    monkeypatch.setattr(os, "system", mock_system_error)

    # Act & Assert
    with pytest.raises(OSError):
        limpiar_pantalla()

def test_limpiar_pantalla_os_name_no_string(monkeypatch):
    """
    Verifica el comportamiento si os.name no es un string (e.g., None), asegurando que no rompa la lógica.
    """
    # Arrange
    comando_ejecutado = None
    def mock_system(comando):
        nonlocal comando_ejecutado
        comando_ejecutado = comando

    monkeypatch.setattr(os, "name", None)
    monkeypatch.setattr(os, "system", mock_system)

    # Act
    limpiar_pantalla()

    # Assert
    assert comando_ejecutado == "clear"