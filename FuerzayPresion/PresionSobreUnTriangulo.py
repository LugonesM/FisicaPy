if __name__ == '__main__':



#Ejersicio del libro: Que presion ejerce sobre un triangulo {20cm base, 3dm altura} una fuerza de 200kg?
  print("¿Que presion ejerse sobre un triangulo   una determinada fuerza?")

  print("Altura del triangulo en dm : ")
  altura = int(input())
  print("base del triangulo en cm : ")
  base = int(input())
  print("Fuerza en kg : ")
  fuerza = int(input())

  altura = altura * 10
  superficie = (altura * base)/2
  presion = fuerza / superficie

  print("La presion sobre el triangulo es fuerza sobre superficie, en este caso : ")
  print(presion, "kg/cm²")  #en el caso del libro 0,6666666
