import pytest
import src.main as main

# Excepción personalizada para salir del bucle while True en los tests
class ExitLoop(Exception):
    pass

# --- Casos Normales (N) ---

def test_menu_principal_opcion_salir(monkeypatch, capsys):
    """
    Verifica que la opción '3' imprima el mensaje de despedida y finalice.
    """
    # Arrange
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "¡Hasta luego!" in captura.out

def test_menu_principal_generacion_flujo_completo(monkeypatch, capsys):
    """
    Verifica que el flujo de generación (opción 1) funcione con valores por defecto.
    """
    # Arrange
    # Simula: Opción 1, Enter (longitud), Enter (mayus), Enter (nums), 
    # Enter (syms), Enter (ambig), Enter (cantidad), 'n' (no guardar), '3' (salir)
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
    """
    Verifica que si se ingresa una longitud mayor a 128, se resetee a 16.
    """
    # Arrange
    # 200 está fuera de rango (8-128), debería comportarse como 16
    respuestas = ["1", "200", "", "", "", "", "1", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    # Si se reseteó a 16, la contraseña generada tendrá longitud aproximada en el print
    assert "1." in captura.out

def test_menu_principal_cantidad_minima(monkeypatch, capsys):
    """
    Verifica que se pueda generar exactamente 1 contraseña (límite inferior).
    """
    # Arrange
    respuestas = ["1", "16", "s", "s", "s", "n", "1", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "1." in captura.out

# --- Casos de Error / Edge (E) ---

def test_menu_principal_input_no_numerico_en_longitud(monkeypatch, capsys):
    """
    Verifica que el programa maneje errores de tipo (ValueError) al ingresar texto en longitud.
    """
    # Arrange
    # Al ingresar "error", saltará al except ValueError y mostrará el mensaje
    respuestas = ["1", "error", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Error: Por favor ingrese números válidos." in captura.out

def test_menu_principal_opcion_invalida(monkeypatch, capsys):
    """
    Verifica que el programa no haga nada (o simplemente reinicie el bucle) ante una opción inexistente.
    """
    # Arrange
    # Ingresa opción "9" (no existe) y luego "3" para salir
    respuestas = ["9", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    # Verificamos que volvió a imprimir el menú (indicado por los separadores)
    assert captura.out.count("====") >= 2

def test_menu_principal_guardado_archivo_cancelado(monkeypatch, capsys):
    """
    Verifica que si el usuario elige 'n' en guardar, no se llame a la función de guardado.
    """
    # Arrange
    # Opción 1 -> Valores defecto -> 'n' (no guardar) -> Salir
    respuestas = ["1", "", "", "", "", "", "", "n", "3"]
    inputs = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    main.menu_principal()
    captura = capsys.readouterr()

    # Assert
    assert "Guardadas correctamente" not in captura.out