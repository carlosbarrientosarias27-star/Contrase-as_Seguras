# test_generator.py — Tests del Generador de Contraseñas

Módulo de pruebas unitarias para verificar el comportamiento de la función `generar_password()` definida en `src/core/generator.py`, usando `pytest` con el patrón **Arrange / Act / Assert**.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `string` | Conjuntos de caracteres para validaciones en los asserts |
| `src.core.generator.generar_password` | Función bajo prueba |

---

# Casos de prueba

### Casos Normales (N)

## `test_generar_password_longitud_por_defecto`

Verifica que la contraseña generada sin argumentos tenga exactamente la longitud por defecto.

| Parámetro | Valor |
|---|---|
| Argumentos | ninguno (valores por defecto) |
| **Resultado esperado** | `len(password) == 16` |

---

## `test_generar_password_solo_minusculas`

Verifica que al desactivar mayúsculas, números y símbolos, la contraseña contenga únicamente letras minúsculas.

| Parámetro | Valor |
|---|---|
| `usar_mayus` | `False` |
| `usar_nums` | `False` |
| `usar_syms` | `False` |
| **Resultado esperado** | Todos los caracteres pertenecen a `string.ascii_lowercase` |

---

## `test_generar_password_excluir_ambiguos`

Verifica que ningún carácter visualmente ambiguo aparezca en la contraseña cuando la opción está activa. Se usa una longitud de 100 para maximizar la probabilidad de detección.

| Parámetro | Valor |
|---|---|
| `longitud` | `100` |
| `excluir_ambiguos` | `True` |
| **Resultado esperado** | Ningún carácter de `"0OI1l"` presente en la contraseña |

---

### Casos Límite (L)

## `test_generar_password_longitud_minima`

Verifica que el generador funcione correctamente con la longitud mínima significativa: un solo carácter.

| Parámetro | Valor |
|---|---|
| `longitud` | `1` |
| **Resultado esperado** | `len(password) == 1` |

---

## `test_generar_password_longitud_extrema`

Verifica la estabilidad y rendimiento del generador ante una longitud muy elevada.

| Parámetro | Valor |
|---|---|
| `longitud` | `1000` |
| **Resultado esperado** | `len(password) == 1000` |

---

### Casos de Borde / Edge

## `test_generar_password_longitud_cero`

Verifica que al solicitar una contraseña de longitud 0, el generador retorne una cadena vacía como resultado natural de `range(0)`.

| Parámetro | Valor |
|---|---|
| `longitud` | `0` |
| **Resultado esperado** | `password == ""` |

---

## `test_generar_password_todos_los_caracteres_activos`

Verifica que la longitud sea la correcta cuando todos los conjuntos de caracteres están habilitados simultáneamente.

| Parámetro | Valor |
|---|---|
| `longitud` | `20` |
| `usar_mayus` | `True` |
| `usar_nums` | `True` |
| `usar_syms` | `True` |
| **Resultado esperado** | `len(password) == 20` |

---

### Casos de Error o Comportamiento Inesperado

## `test_generar_password_longitud_negativa`

Verifica que una longitud negativa produzca una cadena vacía, resultado natural de `range(-5)`.

| Parámetro | Valor |
|---|---|
| `longitud` | `-5` |
| **Resultado esperado** | `password == ""` |

---

## `test_generar_password_error_tipo_longitud`

Verifica que pasar un tipo de dato incorrecto como longitud lance `TypeError`, comportamiento propio de `range()` al recibir un argumento no entero.

| Parámetro | Valor |
|---|---|
| `longitud` | `"dieciseis"` |
| **Excepción esperada** | `TypeError` |

---

## `test_generar_password_excluir_ambiguos_con_solo_numeros`

Verifica que al combinar `excluir_ambiguos=True` con números habilitados, la contraseña no contenga ni `0`, ni `1`, ni ningún otro carácter ambiguo, y que todos los caracteres pertenezcan al pool permitido.

| Parámetro | Valor |
|---|---|
| `longitud` | `50` |
| `usar_mayus` | `False` |
| `usar_nums` | `True` |
| `usar_syms` | `False` |
| `excluir_ambiguos` | `True` |
| **Resultado esperado** | Todos los caracteres pertenecen a minúsculas sin `"l"` + dígitos `"23456789"` |

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_generar_password_longitud_por_defecto` | Normal | Sin argumentos | `len == 16` |
| `test_generar_password_solo_minusculas` | Normal | Solo minúsculas activas | Solo chars `a-z` |
| `test_generar_password_excluir_ambiguos` | Normal | Excluir `0OI1l` con 100 chars | Sin ambiguos |
| `test_generar_password_longitud_minima` | Límite | Longitud `1` | `len == 1` |
| `test_generar_password_longitud_extrema` | Límite | Longitud `1000` | `len == 1000` |
| `test_generar_password_longitud_cero` | Edge | Longitud `0` | `password == ""` |
| `test_generar_password_todos_los_caracteres_activos` | Edge | Todos los sets activos | `len == 20` |
| `test_generar_password_longitud_negativa` | Error | Longitud `-5` | `password == ""` |
| `test_generar_password_error_tipo_longitud` | Error | Longitud `"dieciseis"` | `TypeError` |
| `test_generar_password_excluir_ambiguos_con_solo_numeros` | Error | Ambiguos + nums sin mayus/syms | Solo chars permitidos |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_generator.py

# Con reporte detallado
pytest tests/test_generator.py -v
```