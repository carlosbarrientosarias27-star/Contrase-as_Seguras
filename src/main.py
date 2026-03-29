from src.core.generator import generar_password
from src.core.validator import evaluar_fortaleza
from src.data.storage import guardar_en_archivo
from src.utils.helpers import limpiar_pantalla

def menu_principal():
    """Implementa el bucle principal y menú interactivo."""
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
                # Configuración inicial y validación de rango
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
                    print(f"{i}. {pw} -> [{fort}]")

                if input("\n¿Guardar en archivo? (s/n): ").lower() == 's':
                    guardar_en_archivo(resultados)
                
                input("\nPresione Enter para volver al menú...")
            except ValueError:
                print("Error: Por favor, ingrese un número entero.")
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()