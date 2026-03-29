# test_validator.py — Tests del Evaluador de Fortaleza

Módulo de pruebas unitarias para verificar el comportamiento de la función `evaluar_fortaleza()` definida en `src/core/validator.py`, usando `pytest` con el patrón **Arrange / Act / Assert**.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `string` | Conjuntos de caracteres (disponible para validaciones auxiliares) |
| `src.core.validator.evaluar_fortaleza` | Función bajo prueba |

---

# Recordatorio: escala de puntuación

| Puntuación | Nivel |
|---|---|
| 0 – 2 | `"Débil"` |
| 3 | `"Media"` |
| 4 | `"Fuerte"` |
| 5 | `"Muy fuerte"` |

---

# Casos de prueba

### Casos Normales (N)

## `test_evaluar_fortaleza_muy_fuerte`

Verifica que una contraseña que cumple los 5 criterios retorne `"Muy fuerte"`.

| Parámetro | Valor |
|---|---|
| `password` | `"Ab1!56789012"` |
| Criterios cumplidos | longitud ≥ 12 ✅ · minúsculas ✅ · mayúsculas ✅ · dígitos ✅ · símbolos ✅ |
| Puntuación | 5 |
| **Resultado esperado** | `"Muy fuerte"` |

---

## `test_evaluar_fortaleza_fuerte`

Verifica que una contraseña con 4 criterios (falta símbolo) retorne `"Fuerte"`.

| Parámetro | Valor |
|---|---|
| `password` | `"Password12345"` |
| Criterios cumplidos | longitud ≥ 12 ✅ · minúsculas ✅ · mayúsculas ✅ · dígitos ✅ · símbolos ❌ |
| Puntuación | 4 |
| **Resultado esperado** | `"Fuerte"` |

---

## `test_evaluar_fortaleza_media`

Verifica que una contraseña corta con minúsculas, mayúsculas y dígitos retorne `"Media"`.

| Parámetro | Valor |
|---|---|
| `password` | `"Pass1"` |
| Criterios cumplidos | longitud ≥ 12 ❌ · minúsculas ✅ · mayúsculas ✅ · dígitos ✅ · símbolos ❌ |
| Puntuación | 3 |
| **Resultado esperado** | `"Media"` |

---

## `test_evaluar_fortaleza_debil`

Verifica que una contraseña solo con minúsculas y longitud insuficiente retorne `"Débil"`.

| Parámetro | Valor |
|---|---|
| `password` | `"abcde"` |
| Criterios cumplidos | longitud ≥ 12 ❌ · minúsculas ✅ · mayúsculas ❌ · dígitos ❌ · símbolos ❌ |
| Puntuación | 1 |
| **Resultado esperado** | `"Débil"` |

---

### Casos Límite (L)

## `test_evaluar_fortaleza_longitud_exacta_doce`

Verifica el umbral exacto de longitud: 12 caracteres activan el punto de longitud, pero con solo minúsculas la puntuación total sigue siendo `"Débil"`.

| Parámetro | Valor |
|---|---|
| `password` | `"aaaaaaaaaaaa"` (12 `"a"`) |
| Criterios cumplidos | longitud ≥ 12 ✅ · minúsculas ✅ · resto ❌ |
| Puntuación | 2 |
| **Resultado esperado** | `"Débil"` |

---

## `test_evaluar_fortaleza_longitud_once`

Verifica que con 11 caracteres el criterio de longitud no se activa, resultando en solo 1 punto.

| Parámetro | Valor |
|---|---|
| `password` | `"aaaaaaaaaaa"` (11 `"a"`) |
| Criterios cumplidos | longitud ≥ 12 ❌ · minúsculas ✅ · resto ❌ |
| Puntuación | 1 |
| **Resultado esperado** | `"Débil"` |

---

### Casos de Error / Edge

## `test_evaluar_fortaleza_cadena_vacia`

Verifica que una cadena vacía no cumpla ningún criterio y retorne `"Débil"`.

| Parámetro | Valor |
|---|---|
| `password` | `""` |
| Puntuación | 0 |
| **Resultado esperado** | `"Débil"` |

---

## `test_evaluar_fortaleza_solo_simbolos`

Verifica que una cadena compuesta únicamente de símbolos cortos (longitud < 12) sume solo 1 punto.

| Parámetro | Valor |
|---|---|
| `password` | `"!!!"` |
| Criterios cumplidos | símbolos ✅ · resto ❌ |
| Puntuación | 1 |
| **Resultado esperado** | `"Débil"` |

---

## `test_evaluar_fortaleza_error_tipo_entero`

Verifica que pasar un entero en lugar de una cadena lance `TypeError`, ya que `len()` no acepta tipos no iterables.

| Parámetro | Valor |
|---|---|
| `password` | `12345` |
| **Excepción esperada** | `TypeError` |

---

## `test_evaluar_fortaleza_espacios_en_blanco`

Verifica que los espacios cuenten para la longitud (activan el criterio ≥ 12) pero no sumen puntos en ninguna categoría de caracteres, resultando en solo 1 punto.

| Parámetro | Valor |
|---|---|
| `password` | `" " * 12` (12 espacios) |
| Criterios cumplidos | longitud ≥ 12 ✅ · minúsculas ❌ · mayúsculas ❌ · dígitos ❌ · símbolos ❌ |
| Puntuación | 1 |
| **Resultado esperado** | `"Débil"` |

> Los espacios no pertenecen a `ascii_lowercase`, `ascii_uppercase`, `digits` ni `punctuation` de `string`, por lo que no suman puntos de categoría.

---

# Resumen de casos

| Test | Categoría | Password | Puntuación | Resultado esperado |
|---|---|---|---|---|
| `test_evaluar_fortaleza_muy_fuerte` | Normal | `"Ab1!56789012"` | 5 | `"Muy fuerte"` |
| `test_evaluar_fortaleza_fuerte` | Normal | `"Password12345"` | 4 | `"Fuerte"` |
| `test_evaluar_fortaleza_media` | Normal | `"Pass1"` | 3 | `"Media"` |
| `test_evaluar_fortaleza_debil` | Normal | `"abcde"` | 1 | `"Débil"` |
| `test_evaluar_fortaleza_longitud_exacta_doce` | Límite | `"a" * 12` | 2 | `"Débil"` |
| `test_evaluar_fortaleza_longitud_once` | Límite | `"a" * 11` | 1 | `"Débil"` |
| `test_evaluar_fortaleza_cadena_vacia` | Edge | `""` | 0 | `"Débil"` |
| `test_evaluar_fortaleza_solo_simbolos` | Edge | `"!!!"` | 1 | `"Débil"` |
| `test_evaluar_fortaleza_error_tipo_entero` | Error | `12345` | — | `TypeError` |
| `test_evaluar_fortaleza_espacios_en_blanco` | Edge | `" " * 12` | 1 | `"Débil"` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_validator.py

# Con reporte detallado
pytest tests/test_validator.py -v
```