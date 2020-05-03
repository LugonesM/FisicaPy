import sys 

#Ejercicio del libro: 
#Cuanto pesa un trozo de hierro de 10cm² de base y 4dm de altura, si el peso especifico del hierro es 7,85 g/cm³?

PEH = 7.85 #peso especifico del hierro en g/cm³

def check( value ) :  
 """Chequea si puede convertir las cadena a float:
      Si puede la convierte y retorna eso, 
      Si no puede cierra el programa con un mensaje de:  pone solo numeros
 """
 try:
  float(value)
 except ValueError: 
   print( "pone solo numeros")
   sys.exit()
 return 


def strToFloat( cadena ):
  """Toma un avariable, si es de tipo str reemplaza sus comas, si las tiene, por puntos. 
       Chequea si puede convertir las cadena a float( mediante funcion check) : 
        Si puede la convierte y retorna eso, 
        Si no puede cierra el programa con un mensaje
  """
  if type(cadena) == str :
    cadena = cadena.replace(",",".")  #encuentra las comas en el str y las reemplaza por un punto
    if check(cadena) != 1 :
      cadena=float(cadena)
 return cadena


if __name__ == '__main__':

 print("¿Cuanto pesa un trozo de hierro rectangular?(ponerdecimales detras de un punto)")

 base = input("Base en cm²: ")
 base = strToFloat(base)
 altura = input("Altura en dm : ")
 altura = strToFloat(altura)  

 altura = altura * 10          #paso dm a cm
 volumen = altura * base       #volumen del trozo de hierro en cm³
 peso = PEH * volumen       #formula del peso

 print("Su peso sera de : ")
 print(peso, "g")
 
sys.exit()
