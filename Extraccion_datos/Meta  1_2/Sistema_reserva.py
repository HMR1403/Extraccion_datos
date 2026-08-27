#Hector Malaga Rodriguez 951 27/08/2026
#Un sistema de reservacion de un hotel con sets (en mi ejemplo solo hay 20 habitaciones

h_disponibles = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
h_reservadas = set({})

def reservar(habitacion):
    if habitacion in h_disponibles:
        h_disponibles.remove(habitacion)
        h_reservadas.add(habitacion)
        print(f"Habitacion {habitacion} reservada, aqui tiene sus llaves, que disfrute")
    else:
        print(f"Habitacion {habitacion} no disponible, escoja otra")

def liberar(habitacion):
    if habitacion in h_reservadas:
        h_reservadas.remove(habitacion)
        h_disponibles.add(habitacion)
        print(f"Habitacion {habitacion} liberada, lamentamos que tenga que marcharse, buen viaje")
    else:
        print(f"Habitacion {habitacion} no se encuentra reservada, quizas se equivoco")

def ver():
    print(f"Aquí tienes la lista de habitaciones disponibles:\n\n"
          f"{h_disponibles}\n\n"
          f"Y las que ya estan reservadas:\n\n"
          f"{h_reservadas}")

if __name__ == "__main__":
    reservar(2)
    reservar(3)
    reservar(4)
    reservar(5)
    ver()
    reservar(2)
    reservar(3)
    liberar(4)
    liberar(5)
    ver()
    liberar(4)
    ver()