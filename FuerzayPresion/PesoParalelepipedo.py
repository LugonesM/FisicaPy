if __name__ == '__main__':
#Ejercicio del libro: 
#La base de un paralelepipedo mide 2cm², la presion sobre su base es de 1000kg/m² 
#¿Cual es su peso?
#Resuelvo usando la misma formula de presion igual fuerza sobre superficie
#el peso es la fuerza

  print("¿Que peso tiene un paralelepipedo, sabiendo la superficie de su base y la presion sobre esta?")

  print("superficie de la base en cm² : ")
  base = int(input())
  print("presion sobre la base en kg/m² : ")
  presion = int(input())
  

  presion = presion / 1000
  peso = (presion * base)

  print("El peso del paralelepipedo sera de : ")
  print(peso, "kg fuerza")
