# test_storage.py — Tests del Módulo de Almacenamiento

Módulo de pruebas unitarias para verificar el comportamiento de la función `guardar_en_archivo()` definida en `src/data/storage.py`, usando `pytest` con `monkeypatch` para simular operaciones de escritura en disco sin tocar el sistema de archivos real.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `os` | Manipulación de rutas para el fallback de importación |
| `builtins` | Referencia para parchear `open` con `monkeypatch` |
| `src.data.storage.guardar_en_archivo` | Función bajo prueba |

## Estrategia de importación

El módulo incluye un mecanismo de importación con fallback: intenta primero `from src.data.storage import guardar_en_archivo` y, si falla, ajusta el `sys.path` dinámicamente para localizar el módulo. Esto garantiza compatibilidad al ejecutar los tests desde distintos directorios.

---

# Fixtures y técnicas utilizadas

| Elemento | Descripción |
|---|---|
| `monkeypatch` | Reemplaza `builtins.open` con un objeto `MockFile` para evitar escrituras reales en disco |
| `capsys` | Captura la salida estándar para verificar mensajes de error o confirmación |
| `MockFile` | Clase auxiliar definida en cada test que simula el contexto de apertura de archivo (`__enter__`, `__exit__`, `write`) |

---

# Casos de prueba

### Casos Normales (N)

## `test_guardar_en_archivo_escritura_exitosa`

Verifica que la función escriba el formato correcto al procesar una sola entrada.

| Parámetro | Valor |
|---|---|
| `datos` | `[("Pass123!", "Fuerte")]` |
| **Resultado esperado** | La cadena escrita contiene `"Pass: Pass123! \| Fortaleza: Fuerte"` |

> Se usa `MockFile` para interceptar la llamada a `write()` y capturar el contenido sin crear fichero real.

---

## `test_guardar_en_archivo_multiples_entradas`

Verifica que se llame a `write()` exactamente una vez por cada elemento de la lista.

| Parámetro | Valor |
|---|---|
| `datos` | `[("p1", "Débil"), ("p2", "Media"), ("p3", "Fuerte")]` |
| **Resultado esperado** | `lineas_escritas == 3` |

---

### Casos Límite (L)

## `test_guardar_en_archivo_lista_vacia`

Verifica que al pasar una lista vacía no se realice ninguna escritura en el archivo.

| Parámetro | Valor |
|---|---|
| `datos` | `[]` |
| **Resultado esperado** | `write()` nunca fue llamado (`fue_llamado == False`) |

---

## `test_guardar_en_archivo_modo_append`

Verifica que el archivo se abra siempre en modo `"a"` (append), garantizando que no se sobreescriba el historial previo.

| Parámetro | Valor |
|---|---|
| `datos` | `[("test", "Fuerte")]` |
| **Resultado esperado** | `modo_apertura == "a"` |

> Se intercala un `mock_open` personalizado que registra el modo de apertura antes de retornar el `MockFile`.

---

### Casos de Error / Edge

## `test_guardar_en_archivo_error_permisos`

Verifica que ante un `PermissionError` al abrir el archivo, la función capture la excepción y muestre el mensaje de error en consola sin propagarla.

| Parámetro | Valor |
|---|---|
| `datos` | `[("pw", "Fort")]` |
| Error simulado | `PermissionError("Acceso denegado")` |
| **Resultado esperado** | `"Error al guardar: Acceso denegado"` en `stdout` |

---

## `test_guardar_en_archivo_formato_fecha`

Verifica que cada línea escrita comience con una marca de tiempo en formato `[YYYY-MM-DD ...]`.

| Parámetro | Valor |
|---|---|
| `datos` | `[("pass", "Media")]` |
| **Resultado esperado** | La línea escrita comienza con `"[20"` (prefijo del año actual) |

---

## `test_guardar_en_archivo_tipo_dato_invalido`

Verifica que al pasar `None` como entrada (tipo no iterable), el bloque `try-except` de la función lo capture internamente sin propagar la excepción al llamador.

| Parámetro | Valor |
|---|---|
| `entrada_invalida` | `None` |
| **Resultado esperado** | No se lanza ninguna excepción hacia afuera (`resultado == True`) |

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_guardar_en_archivo_escritura_exitosa` | Normal | Una entrada válida | Formato correcto en `write()` |
| `test_guardar_en_archivo_multiples_entradas` | Normal | Tres entradas | `write()` llamado 3 veces |
| `test_guardar_en_archivo_lista_vacia` | Límite | Lista vacía `[]` | `write()` nunca llamado |
| `test_guardar_en_archivo_modo_append` | Límite | Verificar modo apertura | `modo == "a"` |
| `test_guardar_en_archivo_error_permisos` | Error | `PermissionError` en `open` | Mensaje de error en consola |
| `test_guardar_en_archivo_formato_fecha` | Edge | Verificar marca de tiempo | Línea empieza con `"[20"` |
| `test_guardar_en_archivo_tipo_dato_invalido` | Edge | `None` como entrada | Sin excepción propagada |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_storage.py

# Con reporte detallado
pytest tests/test_storage.py -v
```