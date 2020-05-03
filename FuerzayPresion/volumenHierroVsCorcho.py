import sys 
import math

#Ejercicio del libro: 
#¿Cuantos centimetros cubicos de corcho pesan lo mismo que 200cm³ de hierro?
#peso especifico del hierro es 7,85 g/cm³
#peso especifico corcho 0,22 g/cm³

PEH = 7.85 #peso especifico del hierro en g/cm³
PEC = 0.22 #peso especifico del corcho en g/cm³

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

 if type(cadena) == str:
   cadena = cadena.replace(",",".")  #encuentra las comas en el str y las reemplaza por un punto
   if check(cadena) != 1 :
     cadena=float(cadena)
 return cadena



def calculoPeso(vol, pE ): 
    """calcula el peso en gramos de un material tomando su volumen  (cm³) y peso especifico (g/cm³)"""
  return vol * pE


def calculoVol(peso , pE ):
    """calcula el volumen en cm³ de un material tomando su peso en gramos y su peso especifico (g/cm³)"""
 return peso / pE


if __name__ == '__main__':

 print("¿Cuanto volumen de corcho hay que juntar para igualar el peso de tanto volumen de hierro? (poner decimales detras de un punto)")

 volH = input("volumen de hierro en cm³ : ")
 volH = strToFloat(volH)
  
 pesoH = calculoPeso(volH , PEH )
 volC = calculoVol(pesoH , PEC )
 

 print("El volumen de corcho tendria que ser igual a : ")
 print(volC, "cm³")
sys.exit()
