# helpers.py — Utilidades Auxiliares

Módulo de Python con funciones de apoyo para mejorar la experiencia de uso de la aplicación en terminal.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `os` | Detección del sistema operativo y ejecución de comandos de consola |

Módulo parte de la biblioteca estándar de Python — no requiere dependencias externas.

---

# Funciones

## `limpiar_pantalla()`

Limpia la consola ejecutando el comando nativo del sistema operativo correspondiente, mejorando la legibilidad de la interfaz en terminal.

**No recibe parámetros ni retorna ningún valor.**

| Sistema operativo | Comando ejecutado |
|---|---|
| Windows (`os.name == 'nt'`) | `cls` |
| macOS / Linux | `clear` |

---

# Ejemplo de uso

```python
from helpers import limpiar_pantalla

limpiar_pantalla()
# La consola queda limpia antes de mostrar el siguiente menú
```

---

# Requisitos

- Python 3.14 — no requiere dependencias externas.