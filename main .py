import resource_management as rm
import edificios as ed
import time

paso = 0
while True:
    paso += 1
    print(f"--- Inicio paso {paso} ---")
    ed.edificio()
    print(f"--- Fin paso {paso} ---\n")
    time.sleep(5)
