import pytest
import os 
import sys 

# Asegurar que encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.main as main

# --- CONFIGURACIÓN DE MOCKS ---

@pytest.fixture(autouse=True)
def mock_utils(monkeypatch):
    """Desactiva limpiar_pantalla para que no interfiera con la captura de sys.out."""
    monkeypatch.setattr("src.main.limpiar_pantalla", lambda: None)

# --- TESTS ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """Verifica que la opción '3' salga correctamente."""
    inputs = iter(["3", "3"]) # Añadimos un extra por si acaso
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """Verifica flujo opción 1 con valores por defecto."""
    # 1: opción, ""*6: config, "n": guardar, "3": salir, "3": extra seguridad
    respuestas = ["1", "", "", "", "", "", "", "n", "3", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_longitud_fuera_de_rango_maximo(monkeypatch, capsys):
    """Verifica que longitud 200 se resetee a 16."""
    respuestas = ["1", "200", "", "", "", "", "", "n", "3", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_input_no_numerico_en_longitud(monkeypatch, capsys):
    """Verifica manejo de letras en lugar de números en longitud."""
    # 1: opción, "error": provoca ValueError, "3": salir
    respuestas = ["1", "error", "3", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Error: Por favor, ingrese un número entero." in captura.out

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """Verifica que al responder 'n' no se guarde."""
    respuestas = ["1", "", "", "", "", "", "", "n", "3", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "✅ Guardadas correctamente" not in captura.out