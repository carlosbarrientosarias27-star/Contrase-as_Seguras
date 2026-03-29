import string
import secrets
import os
from datetime import datetime

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

def guardar_en_archivo(passwords_con_fortaleza):
    """
    Escribe cada contraseña con fecha, hora y nivel de fortaleza[cite: 118, 119].
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") [cite: 122]
    try:
        # Abrir archivo en modo append [cite: 119, 122]
        with open("contrasenas.txt", "a") as f:
            for pw, fort in passwords_con_fortaleza:
                f.write(f"[{ahora}] Pass: {pw} | Fortaleza: {fort}\n")
        print("\n✅ Guardadas correctamente en contrasenas.txt") [cite: 120]
    except Exception as e:
        print(f"Error al guardar: {e}")

def limpiar_pantalla():
    """Limpia la consola para mejorar la legibilidad[cite: 129, 132]."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Implementa el bucle principal y menú interactivo[cite: 123, 129, 131]."""
    while True:
        limpiar_pantalla()
        print("========================================")
        print("   GENERADOR DE CONTRASEÑAS SEGURAS    ") 
        print("========================================")
        print("1. Generar contraseñas")
        print("2. Ver historial (Próximamente)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "3":
            print("¡Hasta luego!")
            break
        
        if opcion == "1":
            try:
                # Configuración inicial y validación de rango [cite: 66, 174]
                lon = int(input("Longitud (8-128) [16]: ") or 16)
                if not (8 <= lon <= 128): lon = 16
                
                mayus = input("¿Incluir mayúsculas? (s/n) [s]: ").lower() != 'n'
                nums = input("¿Incluir números? (s/n) [s]: ").lower() != 'n'
                syms = input("¿Incluir símbolos? (s/n) [s]: ").lower() != 'n'
                ambig = input("¿Excluir ambiguos (0,O,1,l)? (s/n) [n]: ").lower() == 's'
                
                # Generación múltiple (1-10) [cite: 93, 97]
                cantidad = int(input("¿Cuántas generar? (1-10) [1]: ") or 1)
                if not (1 <= cantidad <= 10): cantidad = 1
                
                resultados = []
                print("\nContraseñas generadas:")
                for i in range(1, cantidad + 1):
                    pw = generar_password(lon, mayus, nums, syms, ambig)
                    fort = evaluar_fortaleza(pw)
                    resultados.append((pw, fort))
                    print(f"{i}. {pw} -> [{fort}]") [cite: 97, 182]

                if input("\n¿Guardar en archivo? (s/n): ").lower() == 's':
                    guardar_en_archivo(resultados)
                
                input("\nPresione Enter para volver al menú...")
            except ValueError:
                print("Error: Por favor, ingrese un número entero.")
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()