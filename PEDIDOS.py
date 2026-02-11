import threading
import time
import random

# Definimos el cierre para la plancha
# Solo un hilo puede "adquirir" este lock a la vez
lock_plancha = threading.Lock()

def preparar_pedido(nombre_pedido):
    print(f" Pedido recibido: {nombre_pedido}. Esperando turno para la plancha...")
    
    # 2. Sincronizar con Lock()
    # El cocinero intenta usar la plancha
    with lock_plancha:
        print(f" {nombre_pedido} está OCUPANDO la plancha.")
        
        # Simulamos el tiempo de cocción con time.sleep()
        tiempo_coccion = random.uniform(1, 3) 
        time.sleep(tiempo_coccion)
        
        print(f" {nombre_pedido} ha terminado de cocinarse.")
    
    # Una vez fuera del 'with', la plancha queda libre automáticamente
    print(f" {nombre_pedido} listo para servir!")

# 1. Crear un hilo por cada pedido
pedidos = ["Hamburguesa ", "Sándwich de Pollo ", "Bacon Cheeseburger ", "Vegetariana "]
hilos = []

for p in pedidos:
    # Creamos el hilo asignando la función y el argumento
    hilo = threading.Thread(target=preparar_pedido, args=(p,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen (opcional, para orden del programa principal)
for h in hilos:
    h.join()

print("\n ¡Todos los pedidos del turno han sido completados!")