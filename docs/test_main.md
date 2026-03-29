# test_main.py — Tests del Menú Principal

Módulo de pruebas unitarias para verificar el comportamiento de la función `menu_principal()` definida en `src/main.py`, usando `pytest` con `monkeypatch` para simular entradas del usuario y `capsys` para capturar la salida en pantalla.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `os`, `sys` | Ajuste dinámico del `sys.path` para localizar `src` |
| `src.main` | Módulo bajo prueba |

# Ajuste de ruta

El módulo inserta dinámicamente la carpeta raíz del proyecto en `sys.path` para garantizar que `src.main` sea localizable independientemente del directorio desde el que se ejecuten los tests:

```python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

---

# Fixtures

## `mock_utils` *(autouse=True)*

Fixture que se aplica automáticamente a todos los tests del módulo. Desactiva `limpiar_pantalla()` reemplazándola con una función vacía (`lambda: None`) para evitar que limpie la consola durante la captura de salida con `capsys`.

```python
monkeypatch.setattr("src.main.limpiar_pantalla", lambda: None)
```

---

## Convención de entradas simuladas

Dado que `menu_principal()` corre en un `while True`, todas las secuencias de inputs deben terminar con `"3"` (y un `"3"` extra de seguridad) para romper el bucle y evitar que el test quede bloqueado.

**Secuencia tipo para opción 1 (generar):**

```
["1",          # Selecciona opción 1
 "",           # Longitud  → usa default 16
 "",           # Mayúsculas → usa default "s"
 "",           # Números   → usa default "s"
 "",           # Símbolos  → usa default "s"
 "",           # Ambiguos  → usa default "n"
 "",           # Cantidad  → usa default 1
 "n",          # No guardar en archivo
 "3",          # Salir del menú
 "3"]          # Extra de seguridad
```

---

# Casos de prueba

## `test_menu_principal_opcion_salir`

Verifica que seleccionar la opción `"3"` finalice el programa correctamente mostrando el mensaje de despedida.

| Inputs simulados | `["3", "3"]` |
|---|---|
| **Resultado esperado** | `"¡Hasta luego!"` en `stdout` |

---

## `test_menu_principal_generacion_flujo_completo`

Verifica que al seleccionar la opción `"1"` con todos los valores por defecto (inputs vacíos), el flujo de generación se complete correctamente y se muestre la sección de resultados.

| Inputs simulados | `["1", "", "", "", "", "", "", "n", "3", "3"]` |
|---|---|
| Configuración aplicada | Longitud `16`, todas las opciones activas, cantidad `1` |
| **Resultado esperado** | `"Contraseñas generadas:"` en `stdout` |

---

## `test_menu_principal_longitud_fuera_de_rango_maximo`

Verifica que una longitud de `200` (fuera del rango `8-128`) sea silenciosamente corregida a `16` y el flujo continúe normalmente.

| Inputs simulados | `["1", "200", "", "", "", "", "", "n", "3", "3"]` |
|---|---|
| Longitud introducida | `200` → corregida a `16` |
| **Resultado esperado** | `"Contraseñas generadas:"` en `stdout` (sin error) |

---

## `test_menu_principal_input_no_numerico_en_longitud`

Verifica que introducir texto en el campo de longitud dispare el bloque `except ValueError` y muestre el mensaje de error sin colapsar el programa.

| Inputs simulados | `["1", "error", "3", "3"]` |
|---|---|
| Entrada inválida | `"error"` en campo de longitud |
| **Resultado esperado** | `"Error: Por favor, ingrese un número entero."` en `stdout` |

---

## `test_menu_principal_guardado_archivo_cancelado`

Verifica que al responder `"n"` a la pregunta de guardar, no se llame a `guardar_en_archivo()` y el mensaje de confirmación no aparezca en la salida.

| Inputs simulados | `["1", "", "", "", "", "", "", "n", "3", "3"]` |
|---|---|
| Respuesta a guardar | `"n"` |
| **Resultado esperado** | `"✅ Guardadas correctamente"` **no** aparece en `stdout` |

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_menu_principal_opcion_salir` | Normal | Opción `3` directa | `"¡Hasta luego!"` |
| `test_menu_principal_generacion_flujo_completo` | Normal | Flujo completo con defaults | `"Contraseñas generadas:"` |
| `test_menu_principal_longitud_fuera_de_rango_maximo` | Límite | Longitud `200` → corrige a `16` | `"Contraseñas generadas:"` |
| `test_menu_principal_input_no_numerico_en_longitud` | Error | Texto en campo numérico | `"Error: Por favor, ingrese un número entero."` |
| `test_menu_principal_guardado_archivo_cancelado` | Edge | Responde `"n"` al guardar | Sin `"✅ Guardadas correctamente"` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_main.py

# Con reporte detallado
pytest tests/test_main.py -v
```