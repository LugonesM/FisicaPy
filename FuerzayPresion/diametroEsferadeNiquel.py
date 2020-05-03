import sys 
import math

#Ejercicio del libro: 
#Cuanto mide el diametro de una esfera de niquel sabiendo que pesa 2288 kg 
# y que el peso especifico del niquel es 8,6 g/cm³?

PEN = 8.6 #peso especifico del niquel en g/cm³


def check( value ) :  
   """
   Chequea si puede convertir las cadena a float:
      Si puede la convierte y retorna eso, 
      Si no puede cierra el programa con un mensaje de:  pone solo numeros
   """
 try:
  float(value)
 except ValueError: 
   print( "pone solo numeros")
   sys.exit()
  return 

def diametroEsfera(vol):
  """ toma volumen de una esfera (float) y devuelve su diametro (float). """
  radio = ((vol * 3) / (math.pi * 4))**(1./3.) #siguiendo formula para sacar volumen de una esfera = 4/3 * pi * radio³
  return radio * 2


def strToFloat( cadena ):
  """Toma un avariable, si es de tipo str reemplaza sus comas, si las tiene, por puntos. 
      Chequea si puede convertir las cadena a float( mediante funcion check) : 
        Si puede la convierte y retorna eso, 
        Si no puede cierra el programa con un mensaje
  """
 if type(cadena) == str:
   cadena = cadena.replace(",",".")  #encuentra las comas en el str y las reemplaza por un punto
   if check(cadena) != 1 :
     cadena=float(cadena)
 return cadena


if __name__ == '__main__':

 print("¿Cual es el diametro de una esfera de niquel segun su peso?(poner decimales detras de un punto)")

 peso = input("Su peso en kg : ")
 peso = strToFloat(peso)  

 peso = peso * 1000          #paso kg a g
 volumen = peso / PEN      #formula volumen ( en cm³)  = peso / peso especifico del material"
 

 print("Su diametro sera de : ")
 print(diametroEsfera(volumen), "cm") #imprime directo el resultado de la funcion que toma el volumen de la esfera y devuelve su diametro
sys.exit()
