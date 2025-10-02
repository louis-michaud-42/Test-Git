
# diagnostic.py
# Vérification basique du moteur

def check_battery(voltage: float):
    if voltage > 12.0:
        print("🔋 Batterie OK")
    else:
        print("⚠️ Batterie faible !")

def check_fuel(level: int):
    if level > 50:
        print("⛽ Carburant suffisant")
    elif level > 10:
        print("⚠️ Carburant bas")
    else:
        print("❌ Carburant critique !")
