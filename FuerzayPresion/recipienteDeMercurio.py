import sys 

#Ejercicio del libro: 
#Un resipiente de 20cm de largo, 4cm de ancho y 3cm de alto esta lleno de mercurio:
#a) cuanto pesa esa cantidad de mercurio
#b)Cuantos litros de mercurio contiene
#c)cual e a presion en la base

PEM = 13.6 #peso especifico del mercurio en g/cm³


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

 print("Si llenamos de mercurio un recipiente cubico con las siguientes medidas...(poner decimales detras de un punto)")

 largo = input("cm de largo : ")
 largo = strToFloat(largo)
 ancho = input("cm de ancho : ")
 ancho = strToFloat(ancho)
 alto = input("cm de alto : ")
 alto = strToFloat(alto)
  
 litros = (largo*ancho*alto) #para pasarlo a litros
 peso = PEM * litros
 presion = peso / (largo*ancho) #en g/cm²
 
 print("habra ",(litros/1000), " litros de mercurio")
 print("que tendran ", peso , " gramos de peso")
 print("y haran una presion en la base del recipiente ", presion , "g/cm² ")
sys.exit()
