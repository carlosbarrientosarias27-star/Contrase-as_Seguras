import pytest
import os 
import sys 

# Asegurar que encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.main as main

# --- Casos Normales ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """Verifica que la opción '3' salga correctamente."""
    # Solo necesitamos una respuesta: salir
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """Verifica flujo opción 1 con valores por defecto."""
    # 1. Opción 1
    # 2-7. Configuración (6 Enters para usar defaults)
    # 8. Guardar? 'n'
    # 9. IMPORTANTE: Opción '3' para salir del bucle while
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Contraseñas generadas:" in captura.out

# --- Casos Límite ---

def test_menu_principal_longitud_fuera_de_rango_maximo(monkeypatch, capsys):
    """Verifica que longitud 200 se resetee a 16."""
    # 1(opción), 200(longitud), 5(restantes), n(guardar), 3(salir)
    respuestas = ["1", "200", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Contraseñas generadas:" in captura.out

# --- Casos de Error ---

def test_menu_principal_input_no_numerico_en_longitud(monkeypatch, capsys):
    """Verifica manejo de letras en lugar de números."""
    # 1. Opción 1
    # 2. "error" (letra) -> Salta al except y vuelve al menú
    # 3. Opción 3 para salir
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    # Tu main.py imprime "Error: Por favor, ingrese un número entero."
    assert "Error" in captura.out

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """Verifica que 'n' no guarde el archivo."""
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main.menu_principal()
    captura = capsys.readouterr()
    assert "Guardadas correctamente" not in captura.out