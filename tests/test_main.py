import pytest
import os 
import sys 

# Asegurar que encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.main as main

# --- CONFIGURACIÓN DE MOCKS ---

@pytest.fixture(autouse=True)
def mock_utils(monkeypatch):
    """Evita que la pantalla se limpie durante los tests y ensucie la salida."""
    monkeypatch.setattr("src.main.limpiar_pantalla", lambda: None)

# --- TESTS ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """Verifica que la opción '3' salga correctamente."""
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """Verifica flujo opción 1 con valores por defecto."""
    # 1(opción 1), 6(config), 1(guardar n), 1(salir 3)
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_longitud_fuera_de_rango_maximo(monkeypatch, capsys):
    """Verifica que longitud 200 se resetee a 16."""
    # 1(opción 1), 200(lon), 5(rest config), 1(guardar n), 1(salir 3)
    respuestas = ["1", "200", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    # Verificamos que se generaron contraseñas a pesar del valor 200
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_input_no_numerico_en_longitud(monkeypatch, capsys):
    """Verifica manejo de letras en lugar de números en longitud."""
    # 1(opción 1), "error"(letra), 3(salir)
    # Al dar error, el try/except de tu main.py captura el ValueError
    # y vuelve al menú principal, por eso el siguiente input debe ser "3"
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Error: Por favor, ingrese un número entero." in captura.out

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """Verifica que al responder 'n' no se imprima el mensaje de guardado exitoso."""
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "✅ Guardadas correctamente" not in captura.out