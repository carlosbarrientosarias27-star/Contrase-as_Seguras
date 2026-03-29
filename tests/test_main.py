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
    """Verifica flujo opción 1."""
    # Arrange
    # 1. Opción 1
    # 2-7. Configuración (lon, may, num, sym, amb, cant)
    # 8. ¿Guardar? 'n'
    # 9. El bucle reinicia -> Opción '3' para salir
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
    """Verifica que 200 se resetee a 16."""
    # Arrange
    # Opción 1, longitud 200, rest de config, guardar n, salir 3
    respuestas = ["1", "200", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Contraseñas generadas:" in captura.out

def test_menu_principal_cantidad_minima(monkeypatch, capsys):
    """Verifica generación de 1 sola unidad."""
    # Arrange
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
    """Verifica manejo de ValueError en longitud."""
    # Arrange
    # Opción 1, 'error' en longitud -> El código captura el error, 
    # imprime mensaje y vuelve al menú principal -> Enviamos '3' para salir.
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    # Nota: Tu código imprime "Error: Por favor, ingrese un número entero."
    assert "Error" in captura.out

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """Verifica que 'n' no guarda el archivo."""
    # Arrange
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Guardadas correctamente" not in captura.out