# test_helpers.py — Tests del Módulo de Utilidades Auxiliares

Módulo de pruebas unitarias para verificar el comportamiento de la función `limpiar_pantalla()` definida en `src/utils/helpers.py`, usando `pytest` con `monkeypatch` para simular el sistema operativo y los comandos de consola sin ejecutarlos realmente.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `os` | Módulo parcheado para simular `os.name` y `os.system` |
| `src.utils.helpers.limpiar_pantalla` | Función bajo prueba |

---

# Fixtures y técnicas utilizadas

| Elemento | Descripción |
|---|---|
| `monkeypatch` | Reemplaza `os.name` y `os.system` para simular distintos sistemas operativos sin ejecutar comandos reales |
| `mock_system` | Función auxiliar definida en cada test que captura el comando recibido por `os.system` |

---

# Casos de prueba

### Casos Normales (N)

## `test_limpiar_pantalla_ejecuta_comando_windows`

Verifica que al simular un entorno Windows (`os.name == "nt"`), la función llame a `cls`.

| Parámetro simulado | Valor |
|---|---|
| `os.name` | `"nt"` |
| **Resultado esperado** | `comando_ejecutado == "cls"` |

---

## `test_limpiar_pantalla_ejecuta_comando_unix`

Verifica que al simular un entorno Unix/Linux (`os.name == "posix"`), la función llame a `clear`.

| Parámetro simulado | Valor |
|---|---|
| `os.name` | `"posix"` |
| **Resultado esperado** | `comando_ejecutado == "clear"` |

---

### Casos Límite (L)

## `test_limpiar_pantalla_nombre_os_vacio`

Verifica que cuando `os.name` es una cadena vacía `""` (no igual a `"nt"`), la rama `else` se active y se llame a `clear`.

| Parámetro simulado | Valor |
|---|---|
| `os.name` | `""` |
| **Resultado esperado** | `comando == "clear"` |

> Al no coincidir con `"nt"`, el operador ternario evalúa el `else` y selecciona `"clear"`.

---

### Casos de Error / Edge

## `test_limpiar_pantalla_error_en_llamada_sistema`

Verifica que si `os.system` lanza una `OSError` (por ejemplo, fallo del sistema), la excepción se propague correctamente hacia el llamador sin ser suprimida.

| Parámetro simulado | Valor |
|---|---|
| `os.system` | Lanza `OSError("Fallo del sistema")` |
| **Excepción esperada** | `OSError` |

---

## `test_limpiar_pantalla_os_name_no_string`

Verifica que cuando `os.name` es `None` (tipo no esperado), la comparación `os.name == "nt"` evalúe como `False` sin error, y la función seleccione `"clear"` por la rama `else`.

| Parámetro simulado | Valor |
|---|---|
| `os.name` | `None` |
| **Resultado esperado** | `comando_ejecutado == "clear"` |

---

# Resumen de casos

| Test | Categoría | `os.name` simulado | Resultado esperado |
|---|---|---|---|
| `test_limpiar_pantalla_ejecuta_comando_windows` | Normal | `"nt"` | `cls` |
| `test_limpiar_pantalla_ejecuta_comando_unix` | Normal | `"posix"` | `clear` |
| `test_limpiar_pantalla_nombre_os_vacio` | Límite | `""` | `clear` |
| `test_limpiar_pantalla_error_en_llamada_sistema` | Error | — | `OSError` propagada |
| `test_limpiar_pantalla_os_name_no_string` | Edge | `None` | `clear` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_helpers.py

# Con reporte detallado
pytest tests/test_helpers.py -v
```