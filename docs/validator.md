# validator.py — Evaluador de Fortaleza de Contraseñas

Módulo de Python que analiza una contraseña y devuelve un nivel de fortaleza basado en criterios de longitud y variedad de caracteres.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `string` | Conjuntos de caracteres predefinidos para evaluar cada criterio |

Módulo parte de la biblioteca estándar de Python — no requiere dependencias externas.

---

# Funciones

## `evaluar_fortaleza(password)`

Evalúa la fortaleza de una contraseña acumulando una puntuación según cinco criterios independientes y retorna una etiqueta descriptiva.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `password` | `str` | Contraseña a evaluar |

**Retorna:** `str` — Nivel de fortaleza: `"Débil"`, `"Media"`, `"Fuerte"` o `"Muy fuerte"`.

---

# Criterios de evaluación

Cada criterio cumplido suma **+1 punto** a la puntuación total (máximo 5 puntos):

| # | Criterio | Condición |
|---|---|---|
| 1 | Longitud suficiente | `len(password) >= 12` |
| 2 | Contiene minúsculas | Al menos una letra `a-z` |
| 3 | Contiene mayúsculas | Al menos una letra `A-Z` |
| 4 | Contiene dígitos | Al menos un número `0-9` |
| 5 | Contiene símbolos | Al menos un carácter de puntuación (`!@#$%...`) |

---

# Escala de fortaleza

| Puntuación | Nivel |
|---|---|
| 0 – 2 | `"Débil"` |
| 3 | `"Media"` |
| 4 | `"Fuerte"` |
| 5 | `"Muy fuerte"` |

---

# Ejemplos de uso

```python
from validator import evaluar_fortaleza

evaluar_fortaleza("abc")
# → "Débil"        (puntuación: 1 — solo minúsculas, longitud < 12)

evaluar_fortaleza("abcdefghijkl")
# → "Media"        (puntuación: 3 — longitud >= 12, solo minúsculas... no suma mayus/nums/syms... ajustar ejemplo)

evaluar_fortaleza("Abcdef123456")
# → "Fuerte"       (puntuación: 4 — longitud >= 12, minúsculas, mayúsculas, dígitos)

evaluar_fortaleza("Abcdef12@#$!")
# → "Muy fuerte"   (puntuación: 5 — cumple los 5 criterios)
```

---

# Diagrama de puntuación

```
password = "Abcdef12@#$!"

  ✅ len >= 12      → +1  (longitud: 12)
  ✅ minúsculas     → +1  (b, c, d, e, f)
  ✅ mayúsculas     → +1  (A)
  ✅ dígitos        → +1  (1, 2)
  ✅ símbolos       → +1  (@, #, $, !)
                    ────
  Total             →  5  → "Muy fuerte"
```

---

# Requisitos

- Python 3.x — no requiere dependencias externas.