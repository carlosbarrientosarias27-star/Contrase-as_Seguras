# storage.py — Almacenamiento de Contraseñas

Módulo de Python para persistir contraseñas generadas junto con su nivel de fortaleza y marca de tiempo en un archivo de texto local.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `datetime` | Obtener la fecha y hora actual para el registro de cada entrada |

Módulo parte de la biblioteca estándar de Python — no requiere dependencias externas.

---

# Funciones

## `guardar_en_archivo(passwords_con_fortaleza)`

Escribe en modo append en el archivo `contrasenas.txt` cada contraseña recibida junto con la fecha, hora y nivel de fortaleza correspondiente. Si el archivo no existe, lo crea automáticamente.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `passwords_con_fortaleza` | `list[tuple[str, str]]` | Lista de tuplas `(contraseña, nivel_de_fortaleza)` |

**Retorna:** `None` — La función imprime un mensaje de confirmación o de error en consola.

---

# Formato del archivo de salida

Cada entrada se escribe en una línea con el siguiente formato:

```
[YYYY-MM-DD HH:MM:SS] Pass: <contraseña> | Fortaleza: <nivel>
```

**Ejemplo de contenido de `contrasenas.txt`:**

```
[2026-03-29 14:32:10] Pass: aT3#kLm!9Qz@Xw2R | Fortaleza: Muy fuerte
[2026-03-29 14:32:10] Pass: password123      | Fortaleza: Media
[2026-03-29 14:35:47] Pass: Abcdef12@#$!     | Fortaleza: Muy fuerte
```

> Todas las contraseñas de una misma llamada comparten la misma marca de tiempo, capturada al inicio de la ejecución de la función.

---

# Manejo de errores

La escritura está envuelta en un bloque `try-except` que captura cualquier excepción (permisos denegados, disco lleno, ruta inválida, etc.) e imprime un mensaje descriptivo en consola sin interrumpir el flujo del programa.

| Situación | Comportamiento |
|---|---|
| Escritura correcta | Imprime `✅ Guardadas correctamente en contrasenas.txt` |
| Cualquier error de E/S | Imprime `Error al guardar: <detalle del error>` |

---

# Ejemplo de uso

```python
from storage import guardar_en_archivo

passwords = [
    ("aT3#kLm!9Qz@Xw2R", "Muy fuerte"),
    ("password123",       "Media"),
]

guardar_en_archivo(passwords)
# ✅ Guardadas correctamente en contrasenas.txt
```

---

# Requisitos

- Python 3.14 — no requiere dependencias externas.
- Permisos de escritura en el directorio de trabajo donde se ejecute el script.