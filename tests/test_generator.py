import pytest
import string
from src.core.generator import generar_password

# --- Casos Normales (N) ---

def test_generar_password_longitud_por_defecto():
    """
    Verifica que la contraseña generada tenga la longitud por defecto de 16 caracteres.
    """
    # Arrange
    longitud_esperada = 16
    
    # Act
    password = generar_password()
    
    # Assert
    assert len(password) == longitud_esperada

def test_generar_password_solo_minusculas():
    """
    Verifica que si se desactivan mayúsculas, números y símbolos, solo contenga minúsculas.
    """
    # Arrange
    permitidos = string.ascii_lowercase
    
    # Act
    password = generar_password(usar_mayus=False, usar_nums=False, usar_syms=False)
    
    # Assert
    assert all(c in permitidos for c in password)

def test_generar_password_excluir_ambiguos():
    """
    Verifica que no aparezcan caracteres ambiguos (0, O, I, l, 1) cuando la opción está activa.
    """
    # Arrange
    ambiguos = "0OI1l"
    
    # Act
    password = generar_password(longitud=100, excluir_ambiguos=True)
    
    # Assert
    assert not any(c in ambiguos for c in password)

# --- Casos Límite (L) ---

def test_generar_password_longitud_minima():
    """
    Verifica la generación de una contraseña con longitud de 1 carácter.
    """
    # Arrange
    longitud = 1
    
    # Act
    password = generar_password(longitud=longitud)
    
    # Assert
    assert len(password) == 1

def test_generar_password_longitud_extrema():
    """
    Verifica la estabilidad del generador con una longitud grande (e.g., 1000).
    """
    # Arrange
    longitud = 1000
    
    # Act
    password = generar_password(longitud=longitud)
    
    # Assert
    assert len(password) == 1000

# --- Casos de Borde / Edge (E) ---

def test_generar_password_longitud_cero():
    """
    Verifica que solicitar una longitud de 0 devuelva una cadena vacía (comportamiento de range).
    """
    # Arrange
    longitud = 0
    
    # Act
    password = generar_password(longitud=longitud)
    
    # Assert
    assert password == ""

def test_generar_password_todos_los_caracteres_activos():
    """
    Verifica que la longitud sea correcta cuando todos los sets de caracteres están activos.
    """
    # Arrange
    longitud = 20
    
    # Act
    password = generar_password(longitud=20, usar_mayus=True, usar_nums=True, usar_syms=True)
    
    # Assert
    assert len(password) == longitud

# --- Casos de Error o Comportamiento Inesperado (E) ---

def test_generar_password_longitud_negativa():
    """
    Verifica que una longitud negativa resulte en una cadena vacía.
    """
    # Arrange
    longitud = -5
    
    # Act
    password = generar_password(longitud=longitud)
    
    # Assert
    assert password == ""

def test_generar_password_error_tipo_longitud():
    """
    Verifica que se lance un TypeError si la longitud no es un entero (comportamiento de range).
    """
    # Arrange
    longitud = "dieciseis"
    
    # Act & Assert
    with pytest.raises(TypeError):
        generar_password(longitud=longitud)

def test_generar_password_excluir_ambiguos_con_solo_numeros():
    """
    Verifica que no contenga '0' ni '1' (ni 'O', 'I', 'l') al usar números y letras.
    """
    # Arrange
    # Añadimos las minúsculas (menos la 'l') porque el generador las incluye siempre
    letras_sin_l = string.ascii_lowercase.replace("l", "")
    solo_numeros_no_ambiguos = "23456789"
    permitidos = letras_sin_l + solo_numeros_no_ambiguos
    
    # Act
    password = generar_password(longitud=50, usar_mayus=False, usar_nums=True, usar_syms=False, excluir_ambiguos=True)
    
    # Assert
    assert all(c in permitidos for c in password)