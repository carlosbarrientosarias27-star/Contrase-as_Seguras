import pytest
import string
from src.core.validator import evaluar_fortaleza

# --- Casos Normales (N) ---

def test_evaluar_fortaleza_muy_fuerte():
    """
    Verifica que una contraseña con todos los criterios cumpla con 'Muy fuerte'.
    Criterios: longitud >= 12, min, may, num, sym.
    """
    # Arrange
    password_completa = "Ab1!56789012"
    
    # Act
    resultado = evaluar_fortaleza(password_completa)
    
    # Assert
    assert resultado == "Muy fuerte"

def test_evaluar_fortaleza_fuerte():
    """
    Verifica que una contraseña con 4 criterios sea 'Fuerte'.
    """
    # Arrange
    # 4 criterios: min, may, num, longitud >= 12 (falta puntuación)
    password = "Password12345"
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Fuerte"

def test_evaluar_fortaleza_media():
    """
    Verifica que una contraseña con 3 criterios sea 'Media'.
    """
    # Arrange
    # 3 criterios: min, may, num (longitud < 12)
    password = "Pass1"
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Media"

def test_evaluar_fortaleza_debil():
    """
    Verifica que una contraseña con 2 o menos criterios sea 'Débil'.
    """
    # Arrange
    # 2 criterios: min, may
    password = "abcde"
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"

# --- Casos Límite (L) ---

def test_evaluar_fortaleza_longitud_exacta_doce():
    """
    Verifica el umbral de longitud donde 12 caracteres activan el punto extra.
    """
    # Arrange
    # 1 punto por longitud (12) + 1 por minúsculas = 2 puntos
    password = "a" * 12
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"

def test_evaluar_fortaleza_longitud_once():
    """
    Verifica que 11 caracteres no activen el punto de longitud.
    """
    # Arrange
    # 1 punto solo por minúsculas
    password = "a" * 11
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"

# --- Casos de Error / Edge (E) ---

def test_evaluar_fortaleza_cadena_vacia():
    """
    Verifica el comportamiento con una cadena vacía (0 puntos).
    """
    # Arrange
    password = ""
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"

def test_evaluar_fortaleza_solo_simbolos():
    """
    Verifica que una cadena de solo símbolos cortos puntúe correctamente (1 punto).
    """
    # Arrange
    password = "!!!"
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"

def test_evaluar_fortaleza_error_tipo_entero():
    """
    Verifica que se lance TypeError si se pasa un tipo no iterable por len().
    """
    # Arrange
    password = 12345
    
    # Act & Assert
    with pytest.raises(TypeError):
        evaluar_fortaleza(password)

def test_evaluar_fortaleza_espacios_en_blanco():
    """
    Verifica que los espacios cuenten para la longitud pero no para categorías de caracteres.
    """
    # Arrange
    # Longitud 12 (1 pto), pero el espacio no es ascii_lower/upper/digit/punctuation.
    password = " " * 12
    
    # Act
    resultado = evaluar_fortaleza(password)
    
    # Assert
    assert resultado == "Débil"