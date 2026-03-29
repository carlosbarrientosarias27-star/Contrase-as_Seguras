# 🔐 Contraseñas Seguras

Aplicación de línea de comandos desarrollada en Python para generar contraseñas criptográficamente seguras, evaluar su fortaleza y guardarlas en un historial local con marca de tiempo.

---

# 🎯 Objetivos del proyecto

- Generar contraseñas seguras usando el módulo criptográfico `secrets` de Python.
- Evaluar automáticamente la fortaleza de cada contraseña generada.
- Permitir personalización completa: longitud, tipo de caracteres y exclusión de ambiguos.
- Generar múltiples contraseñas en una sola sesión (hasta 10).
- Persistir el historial de contraseñas generadas en un archivo local con fecha y hora.
- Proveer una interfaz de terminal clara, limpia e interactiva.

---

# 📁 Estructura del proyecto

```
CONTRASE-AS_SEGURAS/
├── .github/
│   └── workflows/
│       └── pipeline.yml          # Pipeline de CI/CD
├── docs/
│   ├── asistencia_ia.md          # Registro de prompts utilizados con IA
│   ├── generator.md              # Docs del módulo generator
│   ├── helpers.md                # Docs del módulo helpers
│   ├── main.md                   # Docs del punto de entrada
│   ├── storage.md                # Docs del módulo storage
│   ├── test_generator.md         # Docs de los tests de generator
│   ├── test_helpers.md           # Docs de los tests de helpers
│   ├── test_main.md              # Docs de los tests de main
│   ├── test_storage.md           # Docs de los tests de storage
│   ├── test_validator.md         # Docs de los tests de validator
│   └── validator.md              # Docs del módulo validator
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── generator.py          # Generación de contraseñas seguras
│   │   └── validator.py          # Evaluación de fortaleza
│   ├── data/
│   │   ├── __init__.py
│   │   └── storage.py            # Almacenamiento en archivo local
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py            # Utilidades auxiliares (limpiar pantalla)
│       └── main.py               # Punto de entrada de la aplicación
├── tests/
│   ├── test_generator.py         # Tests del generador
│   ├── test_helpers.py           # Tests de utilidades auxiliares
│   ├── test_main.py              # Tests del menú principal
│   ├── test_storage.py           # Tests del almacenamiento
│   └── test_validator.py         # Tests del evaluador de fortaleza
├── .gitignore
├── conftest.py                   # Configuración global de pytest
├── contrasenas.txt               # Historial de contraseñas generadas
├── LICENSE
├── pytest.ini                    # Configuración de pytest
├── README.md
└── requirements.txt              # Dependencias del proyecto
```

---

# ⚙️ Requisitos

- Python 3.14
- Dependencias listadas en `requirements.txt`

---

# 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/contrasenas-seguras.git
cd contrasenas-seguras
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

# ▶️ Instrucciones de uso

Ejecuta la aplicación desde la raíz del proyecto:

```bash
python main.py
```

Al iniciar verás el menú principal:

```
========================================
   GENERADOR DE CONTRASEÑAS SEGURAS
========================================
1. Generar contraseñas
2. Ver historial (Próximamente)
3. Salir

Seleccione una opción:
```

## Opción 1 — Generar contraseñas

Al seleccionar la opción `1`, la aplicación te guiará por los siguientes parámetros:

| Campo | Rango válido | Default | Descripción |
|---|---|---|---|
| Longitud | `8 – 128` | `16` | Número de caracteres. Fuera de rango → usa `16` |
| Mayúsculas | `s / n` | `s` | Incluye letras `A-Z` |
| Números | `s / n` | `s` | Incluye dígitos `0-9` |
| Símbolos | `s / n` | `s` | Incluye caracteres de puntuación |
| Excluir ambiguos | `s / n` | `n` | Elimina `0`, `O`, `1`, `l`, `I` del pool |
| Cantidad | `1 – 10` | `1` | Contraseñas a generar. Fuera de rango → usa `1` |

> Pulsa **Enter** sin escribir nada para aceptar el valor por defecto de cualquier campo.

## Opción 3 — Salir

Finaliza la aplicación mostrando el mensaje de despedida.

---

# 💡 Ejemplos de uso

## Ejemplo 1 — Contraseña con configuración por defecto

```
Seleccione una opción: 1
Longitud (8-128) [16]:
¿Incluir mayúsculas? (s/n) [s]:
¿Incluir números? (s/n) [s]:
¿Incluir símbolos? (s/n) [s]:
¿Excluir ambiguos (0,O,1,l)? (s/n) [n]:
¿Cuántas generar? (1-10) [1]:

Contraseñas generadas:
1. aT3#kLm!9Qz@Xw2R -> [Muy fuerte]

¿Guardar en archivo? (s/n): n
```

---

## Ejemplo 2 — Varias contraseñas sin símbolos y sin ambiguos

```
Seleccione una opción: 1
Longitud (8-128) [16]: 20
¿Incluir mayúsculas? (s/n) [s]: s
¿Incluir números? (s/n) [s]: s
¿Incluir símbolos? (s/n) [s]: n
¿Excluir ambiguos (0,O,1,l)? (s/n) [n]: s
¿Cuántas generar? (1-10) [1]: 3

Contraseñas generadas:
1. nRk4WmB9pGvX7qTz2cJe -> [Fuerte]
2. hY3sNwD8rFxK5mPa6bVj -> [Fuerte]
3. gC2tMqE7uHzR4nXw9kBs -> [Fuerte]

¿Guardar en archivo? (s/n): s
✅ Guardadas correctamente en contrasenas.txt
```

---

## Ejemplo 3 — Contraseña corta solo con minúsculas

```
Seleccione una opción: 1
Longitud (8-128) [16]: 8
¿Incluir mayúsculas? (s/n) [s]: n
¿Incluir números? (s/n) [s]: n
¿Incluir símbolos? (s/n) [s]: n
¿Excluir ambiguos (0,O,1,l)? (s/n) [n]: n
¿Cuántas generar? (1-10) [1]: 1

Contraseñas generadas:
1. rkmpwbnq -> [Débil]

¿Guardar en archivo? (s/n): n
```

---

# 📄 Historial de contraseñas (`contrasenas.txt`)

Cuando el usuario confirma guardar, cada contraseña se añade al archivo `contrasenas.txt` en modo append con el siguiente formato:

```
[2026-03-29 14:32:10] Pass: aT3#kLm!9Qz@Xw2R | Fortaleza: Muy fuerte
[2026-03-29 14:33:05] Pass: nRk4WmB9pGvX7qTz2cJe | Fortaleza: Fuerte
```

---

# 🧠 Niveles de fortaleza

La fortaleza se evalúa acumulando puntos según 5 criterios independientes:

| Criterio | Condición | Puntos |
|---|---|---|
| Longitud suficiente | `len >= 12` | +1 |
| Contiene minúsculas | Al menos una `a-z` | +1 |
| Contiene mayúsculas | Al menos una `A-Z` | +1 |
| Contiene dígitos | Al menos un `0-9` | +1 |
| Contiene símbolos | Al menos un carácter de puntuación | +1 |

| Puntuación | Nivel |
|---|---|
| 0 – 2 | 🔴 Débil |
| 3 | 🟡 Media |
| 4 | 🟢 Fuerte |
| 5 | 🟢 Muy fuerte |

---

# 🧪 Tests

Ejecuta todos los tests con:

```bash
pytest
```

Con reporte detallado:

```bash
pytest -v
```

| Módulo de test | Función bajo prueba | Nº de casos |
|---|---|---|
| `tests/test_generator.py` | `generar_password` | 10 |
| `tests/test_validator.py` | `evaluar_fortaleza` | 10 |
| `tests/test_storage.py` | `guardar_en_archivo` | 7 |
| `tests/test_helpers.py` | `limpiar_pantalla` | 5 |
| `tests/test_main.py` | `menu_principal` | 5 |
| **Total** | | **37** |

---

# 📦 Módulos

| Módulo | Ruta | Descripción |
|---|---|---|
| `generator` | `src/core/generator.py` | Genera contraseñas con `secrets.choice()` |
| `validator` | `src/core/validator.py` | Evalúa la fortaleza según 5 criterios |
| `storage` | `src/data/storage.py` | Guarda contraseñas en `contrasenas.txt` con timestamp |
| `helpers` | `src/utils/helpers.py` | Limpia la consola de forma multiplataforma |
| `main` | `main.py` | Bucle principal del menú interactivo |

---

# 🔄 CI/CD

El proyecto incluye un pipeline de GitHub Actions (`.github/workflows/pipeline.yml`) que ejecuta automáticamente los tests en cada push o pull request.

---

# 📄 Licencia

Este proyecto está bajo los términos de la licencia incluida en el archivo [LICENSE](LICENSE MIT).