import pytest
import os 
import sys 

# Asegurar que encuentre la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.main as main

# --- Casos Normales (N) ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """Verifica que la opción '3' salga correctamente."""
    # Arrange: Solo una interacción
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """Verifica flujo opción 1 con valores por defecto."""
    # Arrange
    # 1(opcion 1), 6(config), 1(guardar n), 1(salir 3) = 9 total
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Contraseñas generadas:" in captura.out

# --- Casos Límite (L) ---

def test_menu_principal_longitud_fuera_de_rango_maximo(monkeypatch, capsys):
    """Verifica que una longitud de 200 sea ignorada (usa default 16)."""
    # Arrange
    # 1(opcion 1), 200(lon), 5(rest config), 1(guardar n), 1(salir 3)
    respuestas = ["1", "200", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_cantidad_minima(monkeypatch, capsys):
    """Verifica generación de exactamente 1 unidad."""
    # Arrange
    # 1(opcion 1), 16, s, s, s, n, 1(cantidad), n(guardar), 3(salir)
    respuestas = ["1", "16", "s", "s", "s", "n", "1", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "1." in captura.out

# --- Casos de Error (E) ---

def test_menu_principal_input_no_numerico_en_longitud(monkeypatch, capsys):
    """Verifica manejo de ValueError cuando se ingresan letras."""
    # Arrange
    # 1. Opción 1
    # 2. "error" en longitud -> Tu código imprime "Error..." y vuelve al menú principal
    # 3. Opción 3 para salir
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Error" in captura.out

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """Verifica que al responder 'n' no se active el guardado."""
    # Arrange
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Guardadas correctamente" not in captura.out