import pytest
import os
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
    """Verifica que se use 'clear' si os.name está vacío."""
    captura = []
    def mock_run(comando, **kwargs):
        captura.append(comando[0])

    monkeypatch.setattr(subprocess, "run", mock_run)
    monkeypatch.setattr(os, "name", "")

    limpiar_pantalla()
    assert "clear" in captura

# --- Casos de Error / Edge (E) ---

def test_limpiar_pantalla_no_rompe_si_falla_sistema(monkeypatch):
    """Verifica que la función maneje errores de subprocess internamente."""
    def mock_run_error(*args, **kwargs):
        raise RuntimeError("Fallo crítico")

    monkeypatch.setattr(subprocess, "run", mock_run_error)

    # No debe lanzar excepción hacia afuera
    limpiar_pantalla()

def test_limpiar_pantalla_os_name_no_string(monkeypatch):
    """Verifica que maneje casos donde os.name no es un string."""
    captura = []
    def mock_run(comando, **kwargs):
        captura.append(comando[0])

    monkeypatch.setattr(subprocess, "run", mock_run)
    monkeypatch.setattr(os, "name", None)

    limpiar_pantalla()
    assert "clear" in captura