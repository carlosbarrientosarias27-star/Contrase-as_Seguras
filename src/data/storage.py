from datetime import datetime 

def guardar_en_archivo(passwords_con_fortaleza):
    """
    Escribe cada contraseña con fecha, hora y nivel de fortaleza.
    """
    # La fecha se obtiene fuera del bloque try para ser usada en el bucle
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    try:
        # Abrir archivo en modo append ('a')
        with open("contrasenas.txt", "a") as f:
            for pw, fort in passwords_con_fortaleza:
                f.write(f"[{ahora}] Pass: {pw} | Fortaleza: {fort}\n")
        print("\n✅ Guardadas correctamente en contrasenas.txt")
    except Exception as e:
        print(f"Error al guardar: {e}")