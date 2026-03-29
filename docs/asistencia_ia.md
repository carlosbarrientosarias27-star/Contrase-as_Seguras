# 🤖 Asistencia IA — Contraseñas Seguras

Documento que registra el uso de inteligencia artificial (Claude - Anthropic) durante el desarrollo de la documentación del proyecto **Contraseñas Seguras**.

---

# 🛠️ Herramienta utilizada

| Campo | Detalle |
|---|---|
| **IA** | Claude (Anthropic) |
| **Modelo** | Claude Sonnet 4.6 |
| **Interfaz** | claude.ai |
| **Propósito** | Generación de documentación técnica (archivos `.md`) |
| **Fecha** | Marzo 2026 |

---

# 💬 Prompts utilizados

## Prompt 1 — Documentación de `generator.py`

```
Genérame un Readme.md del archivo generator.py
```

**Archivo adjunto:** `generator.py`  
**Resultado obtenido:** `docs/generator.md`  
**Descripción:** Se generó la documentación del módulo generador de contraseñas seguras, incluyendo la descripción de `generar_password()`, tabla de parámetros con valores por defecto, diagrama de construcción acumulativa del pool de caracteres, sección de seguridad explicando el uso de `secrets` frente a `random`, y ejemplos de uso con distintas combinaciones de opciones.

---

## Prompt 2 — Documentación de `test_generator.py`

```
Genérame un Readme.md del archivo test_generator.py
```

**Archivo adjunto:** `test_generator.py`  
**Resultado obtenido:** `docs/test_generator.md`  
**Descripción:** Se generó la documentación del módulo de tests del generador, cubriendo los 10 casos de prueba organizados en 4 categorías (Normal, Límite, Edge, Error), con tablas de parámetros, resultados esperados y notas sobre los comportamientos de borde como longitud `0`, negativa o tipo incorrecto.

---

## Prompt 3 — Documentación de `validator.py`

```
Genérame un Readme.md del archivo validator.py
```

**Archivo adjunto:** `validator.py`  
**Resultado obtenido:** `docs/validator.md`  
**Descripción:** Se generó la documentación del evaluador de fortaleza de contraseñas, incluyendo la tabla de los 5 criterios de evaluación con su condición exacta, la escala de fortaleza con rangos de puntuación (`Débil` / `Media` / `Fuerte` / `Muy fuerte`), ejemplos de uso y un diagrama de puntuación paso a paso.

---

## Prompt 4 — Documentación de `test_validator.py`

```
Genérame un Readme.md del archivo test_validator.py
```

**Archivo adjunto:** `test_validator.py`  
**Resultado obtenido:** `docs/test_validator.md`  
**Descripción:** Se generó la documentación de los 10 casos de prueba del validador, con desglose de qué criterios se cumplen o no (✅/❌) para cada contraseña de prueba, la puntuación resultante y el nivel esperado. Se destacaron los casos límite del umbral de longitud (11 vs 12) y el edge case de espacios en blanco.

---

## Prompt 5 — Documentación de `storage.py`

```
Genérame un Readme.md del archivo storage.py
```

**Archivo adjunto:** `storage.py`  
**Resultado obtenido:** `docs/storage.md`  
**Descripción:** Se generó la documentación del módulo de almacenamiento, detallando el tipo exacto del parámetro (`list[tuple[str, str]]`), el formato de cada línea escrita en `contrasenas.txt`, la nota sobre la marca de tiempo compartida dentro de una misma llamada y la tabla de manejo de errores del bloque `try-except`.

---

## Prompt 6 — Documentación de `test_storage.py`

```
Genérame un Readme.md del archivo test_storage.py
```

**Archivo adjunto:** `test_storage.py`  
**Resultado obtenido:** `docs/test_storage.md`  
**Descripción:** Se generó la documentación de los 7 casos de prueba del módulo de almacenamiento, destacando la técnica de `MockFile` para interceptar `builtins.open` sin tocar el disco, la estrategia de importación con fallback, y casos como error de permisos, modo append, lista vacía y entradas inválidas.

---

## Prompt 7 — Documentación de `helpers.py`

```
Genérame un Readme.md del archivo helpers.py
```

**Archivo adjunto:** `helpers.py`  
**Resultado obtenido:** `docs/helpers.md`  
**Descripción:** Se generó la documentación del módulo de utilidades auxiliares, incluyendo el comportamiento multiplataforma de `limpiar_pantalla()` con la tabla `Windows → cls` / `macOS·Linux → clear` y un ejemplo de uso.

---

## Prompt 8 — Documentación de `test_helpers.py`

```
Genérame un Readme.md del archivo test_helpers.py
```

**Archivo adjunto:** `test_helpers.py`  
**Resultado obtenido:** `docs/test_helpers.md`  
**Descripción:** Se generó la documentación de los 5 casos de prueba del módulo de helpers, con tabla de `os.name` simulado y resultado esperado para cada caso. Se destacó la explicación de los casos límite (cadena vacía activa el `else`) y el edge case de `None` como valor de `os.name`.

---

## Prompt 9 — Documentación de `main.py`

```
Genérame un Readme.md del archivo main.py
```

**Archivo adjunto:** `main.py`  
**Resultado obtenido:** `docs/main.md`  
**Descripción:** Se generó la documentación del punto de entrada principal de la aplicación, incluyendo la tabla de dependencias internas con el rol de cada módulo, el diagrama de flujo completo del bucle con sus vías de salida, la tabla de parámetros configurables con rangos y valores por defecto, un ejemplo de sesión interactiva completa y la tabla de manejo automático de errores.

---

## Prompt 10 — Documentación de `test_main.py`

```
Genérame un Readme.md del archivo test_main.py
```

**Archivo adjunto:** `test_main.py`  
**Resultado obtenido:** `docs/test_main.md`  
**Descripción:** Se generó la documentación de los 5 casos de prueba del menú principal, destacando el fixture `mock_utils` con `autouse=True` que desactiva `limpiar_pantalla()` globalmente, la convención de entradas simuladas comentada campo a campo y la necesidad de terminar siempre con `"3"` para romper el `while True`.

---

## Prompt 11 — Documento de asistencia IA

```
Creame un asistencia_ia.md del proyecto contraseña_seguras de los prompts que utilice
```

**Archivo adjunto:** Capturas de pantalla de la estructura del proyecto en VS Code  
**Resultado obtenido:** `docs/asistencia_ia.md`  
**Descripción:** Se generó el presente documento, registrando todos los prompts utilizados durante la sesión, los archivos adjuntos proporcionados y los resultados obtenidos en cada interacción.

---

# 📊 Resumen de interacciones

| # | Prompt | Adjunto | Resultado |
|---|---|---|---|
| 1 | Documentación de `generator.py` | `generator.py` | `docs/generator.md` |
| 2 | Documentación de `test_generator.py` | `test_generator.py` | `docs/test_generator.md` |
| 3 | Documentación de `validator.py` | `validator.py` | `docs/validator.md` |
| 4 | Documentación de `test_validator.py` | `test_validator.py` | `docs/test_validator.md` |
| 5 | Documentación de `storage.py` | `storage.py` | `docs/storage.md` |
| 6 | Documentación de `test_storage.py` | `test_storage.py` | `docs/test_storage.md` |
| 7 | Documentación de `helpers.py` | `helpers.py` | `docs/helpers.md` |
| 8 | Documentación de `test_helpers.py` | `test_helpers.py` | `docs/test_helpers.md` |
| 9 | Documentación de `main.py` | `main.py` | `docs/main.md` |
| 10 | Documentación de `test_main.py` | `test_main.py` | `docs/test_main.md` |
| 11 | Documento de asistencia IA | Capturas VS Code | `docs/asistencia_ia.md` |

---

# ✅ Observaciones

- Todos los prompts fueron directos y orientados a un archivo o entregable concreto.
- La IA infirió el contexto del proyecto (generador de contraseñas seguras, arquitectura modular `src/core`, `src/data`, `src/utils`) a partir del código fuente adjunto en cada interacción.
- Los archivos de código fuente (`.py`) y capturas de pantalla de VS Code fueron los únicos adjuntos utilizados.
- No fue necesario iterar ni corregir ningún prompt; cada interacción produjo el resultado esperado en un solo intento.
- La cobertura de documentación alcanzada es total: módulos de negocio (`generator`, `validator`), datos (`storage`), utilidades (`helpers`), punto de entrada (`main`) y todos sus módulos de tests correspondientes.