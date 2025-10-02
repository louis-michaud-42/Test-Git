
# main.py
# Programme principal

from engine import start_engine, stop_engine, engine_status
from diagnostic import check_battery, check_fuel

if __name__ == "__main__":
    print("🚀 Simulation du moteur de compétition ACE")

    running = start_engine()
    engine_status(running)

    print("\n--- Vérifications ---")
    check_battery(11.5)
    check_fuel(5)

    running = stop_engine()
    engine_status(running)
