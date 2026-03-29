import string
import secrets

def generar_password(longitud=16, usar_mayus=True, usar_nums=True, usar_syms=True, excluir_ambiguos=False):
    """
    Genera una contraseña segura utilizando el módulo secrets[cite: 15, 195].
    """
    # Construcción dinámica según opciones [cite: 74, 75]
    caracteres = string.ascii_lowercase
    if usar_mayus: caracteres += string.ascii_uppercase
    if usar_nums: caracteres += string.digits
    if usar_syms: caracteres += string.punctuation

    # Filtrar caracteres ambiguos: 0, O, I, l, 1 [cite: 102, 106]
    if excluir_ambiguos:
        for c in "0OI1l":
            caracteres = caracteres.replace(c, "")

    # Uso de secrets para seguridad criptográfica [cite: 195, 196]
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))