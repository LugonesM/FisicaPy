if __name__ == '__main__':
#Ejercicio del libro: 
#La presion que ejerce sobre una superficie un cuerpo que pesa 1 tonelada es 50 kg/cm²
#¿Cuanto mide la superficie?

  
 print("¿Cuanto mide la superficie de un cuerpo con cierto peso si su presion es tanta?")

 peso = float(input("Peso del cuerpo en toneladas: "))
 presion = float(input("presion sobre la base en kg/cm² "))
 
#Resulevo usando misma formula presion igual fuerza sobre superficie
 peso = peso * 1000
 superficie = peso / presion

 print("La superficie del cuerpo sera de : ")
 print(superficie, "cm²") #20cm² en ejemplo de libro
