from datetime import datetime 

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