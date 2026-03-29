import pytest
import os 
import sys 

# Asegurar que encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.main as main

# --- Casos Normales (N) ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """Verifica que la opción '3' salga correctamente."""
    # Arrange
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """Verifica flujo opción 1: 7 inputs de config + 1 de guardar + 1 de salir."""
    # Arrange
    # 1(opcion) + 6(config: lon, may, num, sym, amb, cant) + 1(guardar) + 1(salir)
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Contraseñas generadas:" in captura.out

# --- Casos Límite (L) ---

def test_menu_principal_cantidad_minima(monkeypatch, capsys):
    """Verifica generación de 1 sola unidad."""
    # Arrange
    # Opción 1, defaults, cantidad 1, no guardar, salir
    respuestas = ["1", "16", "s", "s", "s", "n", "1", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "1." in captura.out

# --- Casos de Error (E) ---

def test_menu_principal_input_no_numerico(monkeypatch, capsys):
    """Verifica manejo de error al meter letras en longitud."""
    # Arrange
    # Opción 1, 'error' en longitud (lanza ValueError), 3 para salir
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Error: Por favor ingrese números válidos." in captura.out

def test_menu_principal_opcion_invalida(monkeypatch, capsys):
    """Verifica que opción inexistente reinicie el menú."""
    # Arrange
    respuestas = ["9", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    # Buscamos el título del menú que se repite al reentrar al bucle
    assert "GENERADOR DE CONTRASEÑAS" in captura.out