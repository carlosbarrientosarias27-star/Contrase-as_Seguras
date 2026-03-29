# main.py — Punto de Entrada del Generador de Contraseñas

Archivo principal de la aplicación. Implementa el bucle de menú interactivo que integra la generación, evaluación y almacenamiento de contraseñas seguras mediante los módulos del proyecto.

---

# Dependencias internas

| Módulo | Función importada | Rol |
|---|---|---|
| `src.core.generator` | `generar_password` | Genera contraseñas criptográficamente seguras |
| `src.core.validator` | `evaluar_fortaleza` | Evalúa el nivel de fortaleza de cada contraseña |
| `src.data.storage` | `guardar_en_archivo` | Persiste las contraseñas en `contrasenas.txt` |
| `src.utils.helpers` | `limpiar_pantalla` | Limpia la consola antes de mostrar el menú |

---

# Funciones

## `menu_principal()`

Lanza el bucle principal de la aplicación con un menú interactivo en terminal. Coordina la configuración del usuario, la generación múltiple de contraseñas, su evaluación y el guardado opcional en archivo.

**No recibe parámetros ni retorna ningún valor.**

---

# Flujo de ejecución

```
┌─────────────────────────────────────────┐
│       Inicio del bucle (while True)     │
└────────────────────┬────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │    Limpia pantalla    │
         │    Muestra menú       │
         │  1. Generar           │
         │  2. Historial (soon)  │
         │  3. Salir             │
         └──────────┬────────────┘
                    │
         ┌──────────▼────────────┐
         │    ¿Opción 3?        │──── Sí ──► "¡Hasta luego!" → FIN
         └──────────┬────────────┘
                    │ No (opción 1)
                    ▼
         ┌───────────────────────┐
         │  Configuración:       │
         │  · Longitud (8-128)   │
         │  · Mayúsculas (s/n)   │
         │  · Números (s/n)      │
         │  · Símbolos (s/n)     │
         │  · Excluir ambiguos   │
         │  · Cantidad (1-10)    │
         └──────────┬────────────┘
                    │
                    ▼
         ┌───────────────────────┐
         │  Genera y evalúa      │
         │  cada contraseña      │
         │  → generar_password() │
         │  → evaluar_fortaleza()│
         └──────────┬────────────┘
                    │
                    ▼
         ┌───────────────────────┐
         │ ¿Guardar en archivo? │
         └──────────┬────────────┘
              Sí    │    No
               ▼    │     ▼
    guardar_en_archivo()  │
                    │─────┘
                    ▼
         ┌───────────────────────┐
         │  Enter para volver    │
         └──────────┬────────────┘
                    │
                    └──────────────► Vuelve al inicio del bucle
```

---

# Parámetros de configuración

| Campo | Rango válido | Valor por defecto | Descripción |
|---|---|---|---|
| Longitud | `8 – 128` | `16` | Número de caracteres de cada contraseña. Fuera de rango → usa `16` |
| Mayúsculas | `s / n` | `s` | Incluye letras `A-Z` |
| Números | `s / n` | `s` | Incluye dígitos `0-9` |
| Símbolos | `s / n` | `s` | Incluye caracteres de puntuación |
| Excluir ambiguos | `s / n` | `n` | Elimina `0`, `O`, `1`, `l`, `I` del pool |
| Cantidad | `1 – 10` | `1` | Número de contraseñas a generar. Fuera de rango → usa `1` |

---

# Ejemplo de sesión interactiva

```
========================================
   GENERADOR DE CONTRASEÑAS SEGURAS
========================================
1. Generar contraseñas
2. Ver historial (Próximamente)
3. Salir

Seleccione una opción: 1
Longitud (8-128) [16]: 20
¿Incluir mayúsculas? (s/n) [s]: s
¿Incluir números? (s/n) [s]: s
¿Incluir símbolos? (s/n) [s]: s
¿Excluir ambiguos (0,O,1,l)? (s/n) [n]: n
¿Cuántas generar? (1-10) [1]: 3

Contraseñas generadas:
1. aT3#kLm!9Qz@Xw2R$vN -> [Muy fuerte]
2. Pb7!rQw@5Yz#Mn2Xs$tK -> [Muy fuerte]
3. Hj4@Lk9!Qr#Mn7Xp$Yw2 -> [Muy fuerte]

¿Guardar en archivo? (s/n): s
✅ Guardadas correctamente en contrasenas.txt

Presione Enter para volver al menú...
```

---

# Manejo de errores

| Situación | Comportamiento |
|---|---|
| Longitud fuera de rango (< 8 o > 128) | Se asigna `16` automáticamente |
| Cantidad fuera de rango (< 1 o > 10) | Se asigna `1` automáticamente |
| Entrada no numérica en longitud o cantidad | Captura `ValueError` y muestra aviso; el bucle continúa |

---

# Requisitos

- Python 3.14
- Módulos internos: `src.core`, `src.data` y `src.utils` deben estar accesibles en el `PYTHONPATH`.

---

# Ejecución

```bash
python main.py
```