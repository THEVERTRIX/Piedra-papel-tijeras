# Juego de piedra papel o tijeras en python
import random
import os
import time

# Objetos disponibles
obj = [
    {"name": "Papel", "value": 1},
    {"name": "Tijera", "value": 2},
    {"name": "Piedra", "value": 3},
]

# Contador de veces ganadas
stats = [{"Cpu-wins": 0}, {"User-wins": 0}]

print("Hola! bienvenido a Piedra, Papel o tijeras.")

# Mientras sea verdadero y los datos no sean los correctos repetira el mensaje
while True:
    try:
        rondas = int(input("Elije cuantas rondas seran: "))
        veces = int(input("Veces por ronda: "))
        break
    except:
        print("Por favor ingrese una cantidad valida")
        time.sleep(2)
        os.system("clear")

# Se repetira el proceso hasta que terminen todas las veces por rondas
for x in range(veces * rondas):
    os.system("clear")

    eleccion = int(input("Elije(1-3)\n1 = Papel\n2 = Tijera\n3 = Piedra\n\nEleccion: "))
    sel_cpu = random.choice(obj)
    cpu = sel_cpu["value"]

    print("\nCPU eligio: ", sel_cpu["name"])

    # Verifica los valores, muestra el ganador y termina agregando un punto al ganador
    # 1 = papel
    # 2 = tijeras
    # 3 = piedra
    if cpu == eleccion:
        print("\nResultado: empate, No pasa nada")
    elif cpu == 3 and eleccion == 2:
        stats[0]["Cpu-wins"] += 1
        print("\nResultado: CPU gana, Piedra rompe tijeras")
    elif cpu == 2 and eleccion == 1:
        stats[0]["Cpu-wins"] += 1
        print("\nResultado: CPU gana, Tijeras rompe papel")
    elif cpu == 1 and eleccion == 3:
        stats[0]["Cpu-wins"] += 1
        print("\nResultado: CPU gana, Papel envuelve piedra")
    elif eleccion == 3 and cpu == 2:
        stats[1]["User-wins"] += 1
        print("\nResultado: Tu ganas, Piedra rompe tijeras")
    elif eleccion == 2 and cpu == 1:
        stats[1]["User-wins"] += 1
        print("\nResultado: Tu ganas, Tijeras rompe papel")
    elif eleccion == 1 and cpu == 3:
        stats[1]["User-wins"] += 1
        print("\nResultado: CPU gana, Papel envuelve piedra")
    else:
        print("No es una eleccion correcta!")

    time.sleep(3)

# Mostrara el ganador con mayor puntaje
if stats[0]["Cpu-wins"] > stats[1]["User-wins"]:
    print("\nResultado final: Cpu Gana")
elif stats[0]["Cpu-wins"] < stats[1]["User-wins"]:
    print("\nResultado final: Tu Ganas")
else:
    print("\nResultado final: Empate")

# Muestra el puntaje de ambos
print("Tu puntaje: %d\nPuntaje de la cpu: %d" % (stats[1]["User-wins"], stats[0]["Cpu-wins"]))
