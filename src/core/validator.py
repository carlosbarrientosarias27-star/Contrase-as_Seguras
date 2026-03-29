import string

def evaluar_fortaleza(password):
    """
    Evalúa la fortaleza de una contraseña basándose en criterios de longitud
    y variedad de caracteres[cite: 80, 84].
    """
    puntuacion = 0
    longitud = len(password)

    # Criterios: longitud, presencia de tipos de caracteres [cite: 85]
    if longitud >= 12: puntuacion += 1
    if any(c in string.ascii_lowercase for c in password): puntuacion += 1
    if any(c in string.ascii_uppercase for c in password): puntuacion += 1
    if any(c in string.digits for c in password): puntuacion += 1
    if any(c in string.punctuation for c in password): puntuacion += 1

    # Devolver una puntuación: Débil / Media / Fuerte / Muy fuerte [cite: 86]
    if puntuacion <= 2: return "Débil"
    if puntuacion == 3: return "Media"
    if puntuacion == 4: return "Fuerte"
    return "Muy fuerte"