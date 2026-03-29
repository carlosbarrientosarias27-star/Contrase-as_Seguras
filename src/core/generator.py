import string
import secrets

def generar_password(longitud=16, usar_mayus=True, usar_nums=True, usar_syms=True, excluir_ambiguos=False):
    """
    Genera una contraseña segura utilizando el módulo secrets.
    Referencias: [secrets: 15, 195]
    """
    # Construcción dinámica según opciones [referencia: 74, 75]
    caracteres = string.ascii_lowercase
    if usar_mayus: caracteres += string.ascii_uppercase
    if usar_nums: caracteres += string.digits
    if usar_syms: caracteres += string.punctuation

    # Filtrar caracteres ambiguos: 0, O, I, l, 1 [referencia: 102, 106]
    if excluir_ambiguos:
        for c in "0OI1l":
            caracteres = caracteres.replace(c, "")

    # Uso de secrets para seguridad criptográfica [referencia: 195, 196]
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))