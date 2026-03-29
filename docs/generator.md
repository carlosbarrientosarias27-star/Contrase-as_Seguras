# generator.py — Generador de Contraseñas Seguras

Módulo de Python para la generación de contraseñas criptográficamente seguras mediante el módulo estándar `secrets`. Permite personalizar la composición de la contraseña a través de múltiples parámetros opcionales.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `string` | Conjuntos de caracteres predefinidos (letras, dígitos, puntuación) |
| `secrets` | Generación de valores aleatorios criptográficamente seguros |

Ambos módulos son parte de la biblioteca estándar de Python — no requiere dependencias externas.

---

# Funciones

## `generar_password(longitud, usar_mayus, usar_nums, usar_syms, excluir_ambiguos)`

Genera una contraseña segura construyendo dinámicamente el conjunto de caracteres permitidos según las opciones indicadas y seleccionando cada carácter con `secrets.choice()`.

## Parámetros

| Parámetro | Tipo | Valor por defecto | Descripción |
|---|---|---|---|
| `longitud` | `int` | `16` | Número de caracteres de la contraseña |
| `usar_mayus` | `bool` | `True` | Incluye letras mayúsculas (`A-Z`) |
| `usar_nums` | `bool` | `True` | Incluye dígitos (`0-9`) |
| `usar_syms` | `bool` | `True` | Incluye símbolos de puntuación (`!"#$%&...`) |
| `excluir_ambiguos` | `bool` | `False` | Excluye caracteres visualmente confusos: `0`, `O`, `I`, `1`, `l` |

**Retorna:** `str` — La contraseña generada.

---

# Construcción del conjunto de caracteres

El pool de caracteres se construye de forma acumulativa según las opciones activas:

```
Base siempre incluida → letras minúsculas (a-z)
+ usar_mayus = True   → letras mayúsculas (A-Z)
+ usar_nums  = True   → dígitos (0-9)
+ usar_syms  = True   → símbolos de puntuación (!@#$%...)
─────────────────────────────────────────────────────────
excluir_ambiguos = True → elimina del pool: 0, O, I, 1, l
```

---

# Seguridad

A diferencia de `random`, el módulo `secrets` está diseñado para uso criptográfico, lo que hace que las contraseñas generadas sean adecuadas para aplicaciones que requieren alta seguridad, como tokens de autenticación, claves de API o contraseñas de usuario.

---

# Ejemplos de uso

```python
from generator import generar_password

# Contraseña con configuración por defecto (16 caracteres, todos los tipos)
generar_password()
# → "aT3#kLm!9Qz@Xw2R"

# Contraseña solo con letras minúsculas y números, 12 caracteres
generar_password(longitud=12, usar_mayus=False, usar_syms=False)
# → "g4k1n8m3p7q2"

# Contraseña sin caracteres ambiguos para mayor legibilidad
generar_password(longitud=20, excluir_ambiguos=True)
# → "aX7#nMw@3eKp!vZr9qTd"

# Contraseña corta solo con minúsculas y mayúsculas
generar_password(longitud=8, usar_nums=False, usar_syms=False)
# → "gTkNwXaP"
```

---

# Requisitos

- Python 3.14 — `secrets` está disponible desde esta versión.