nombre1 = input("Como se llamara el jugador 1? ")
nombre2 = input("Como se llamara el jugador 2? ")

jugador1 = input("Hola jugador1! que eliges? Piedra, papel o tijera?: ")
jugador2 = input("Hola jugador2! que eliges? Piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"


if jugador1 == jugador2:
    print("Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)


# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minuscula con minuscula
# Mas de 1 turno con el bucle While
# Desafio