
# engine.py
# Gestion très basique d'un moteur

def start_engine():
    print("🔑 Mise en marche du moteur...")
    return True

def stop_engine():
    print("🛑 Arrêt du moteur...")
    return False

def engine_status(running: bool):
    if running:
        print("✅ Le moteur est en marche !")
    else:
        print("❌ Le moteur est arrêté.")
