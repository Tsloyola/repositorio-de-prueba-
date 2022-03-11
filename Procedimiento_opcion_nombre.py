#Procedimiento para elegir la opcion con la que se jugara
def elegir_opcion():
  accion_usuario = input("Ingresa una opción: (piedra, papel, tijera):")
  accion_computadora=eleccion_computadora()
  comparacion_resultados(accion_usuario,accion_computadora)


#Procedimiento para preguntarle el nombre al usuario
def preguntar_nombre():
  print("")
  nombre = input("Primero ingresa tu nombre: ")
  cleaning()
  print("")
  print(f"Hola {nombre}!, bienvenido al juego de piedra, papel o tijera \n")
