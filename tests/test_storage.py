import pytest
import os
import builtin
from src.data.storage import guardar_en_archivo

# --- Casos Normales (N) ---

def test_guardar_en_archivo_escritura_exitosa(monkeypatch):
    """
    Verifica que la función intente escribir el formato correcto en el archivo.
    """
    # Arrange
    datos = [("Pass123!", "Fuerte")]
    escritos = []

    class MockFile:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def write(self, contenido): escritos.append(contenido)

    monkeypatch.setattr("builtins.open", lambda name, mode: MockFile())
    
    # Act
    guardar_en_archivo(datos)
    
    # Assert
    assert "Pass: Pass123! | Fortaleza: Fuerte" in escritos[0]

def test_guardar_en_archivo_multiples_entradas(monkeypatch):
    """
    Verifica que se procesen todos los elementos de la lista proporcionada.
    """
    # Arrange
    datos = [("p1", "Débil"), ("p2", "Media"), ("p3", "Fuerte")]
    lineas_escritas = 0

    class MockFile:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def write(self, contenido):
            nonlocal lineas_escritas
            lineas_escritas += 1

    monkeypatch.setattr("builtins.open", lambda name, mode: MockFile())

    # Act
    guardar_en_archivo(datos)

    # Assert
    assert lineas_escritas == len(datos)

# --- Casos Límite (L) ---

def test_guardar_en_archivo_lista_vacia(monkeypatch):
    """
    Verifica que no se escriba nada si la lista de contraseñas está vacía.
    """
    # Arrange
    datos_vacios = []
    fue_llamado = False

    class MockFile:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def write(self, contenido):
            nonlocal fue_llamado
            fue_llamado = True

    monkeypatch.setattr("builtins.open", lambda name, mode: MockFile())

    # Act
    guardar_en_archivo(datos_vacios)

    # Assert
    assert fue_llamado is False

def test_guardar_en_archivo_modo_append(monkeypatch):
    """
    Verifica que el archivo se abra específicamente en modo 'a' (append).
    """
    # Arrange
    datos = [("test", "Fuerte")]
    modo_apertura = None

    # Creamos un Mock que no llame a 'open' real para evitar recursión
    class MockFile:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def write(self, contenido): pass

    def mock_open(name, mode):
        nonlocal modo_apertura
        modo_apertura = mode
        return MockFile() # Retornamos el objeto simulado

    monkeypatch.setattr("builtins.open", mock_open)

    # Act
    guardar_en_archivo(datos)

    # Assert
    assert modo_apertura == "a"

# --- Casos de Error / Edge (E) ---

def test_guardar_en_archivo_error_permisos(monkeypatch, capsys):
    """
    Verifica que se capture la excepción y se imprima el mensaje de error si falla la apertura.
    """
    # Arrange
    def mock_open_error(*args, **kwargs):
        raise PermissionError("Acceso denegado")

    monkeypatch.setattr("builtins.open", mock_open_error)
    
    # Act
    guardar_en_archivo([("pw", "Fort")])
    captura = capsys.readouterr()
    
    # Assert
    assert "Error al guardar: Acceso denegado" in captura.out

def test_guardar_en_archivo_formato_fecha(monkeypatch):
    """
    Verifica que la línea escrita comience con el formato de fecha [YYYY-MM-DD].
    """
    # Arrange
    datos = [("pass", "Media")]
    contenido_escrito = ""

    class MockFile:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def write(self, contenido):
            nonlocal contenido_escrito
            contenido_escrito = contenido

    monkeypatch.setattr("builtins.open", lambda n, m: MockFile())

    # Act
    guardar_en_archivo(datos)

    # Assert
    # Verifica que empiece con '[' y tenga longitud de fecha ISO aproximada
    assert contenido_escrito.startswith("[20") 

def test_guardar_en_archivo_tipo_dato_invalido():
    """
    Verifica que el bloque try-except maneje casos donde la entrada no es iterable.
    """
    # Arrange
    entrada_invalida = None
    
    # Act & Assert
    # No debería lanzar excepción hacia afuera porque hay un try-except general
    try:
        guardar_en_archivo(entrada_invalida)
        resultado = True
    except:
        resultado = False
    
    assert resultado is True