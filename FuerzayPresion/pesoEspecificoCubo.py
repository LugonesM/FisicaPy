import sys 

#Ejercicio del libro: 
#Cubo de 5cm de arista pesa 2,625kg
#¿Cual es su peso especifico?

def check( value ) :   #funcion que chequea que el usuario ingreso valores posibles para la cuenta 
 try:
  float(value)
 except ValueError:  #de no ser asi imprime un mensaje de error y sale del programa
   print( "pone solo numeros boludoo")
   sys.exit()
 return 

def strToFloat( cadena ):
 if type(cadena) == str :
   cadena = cadena.replace(",",".")  #encuentra las comas en el str y las reemplaza por un punto
   if check(cadena) != 1 :
     cadena=float(cadena)
 return cadena


if __name__ == '__main__':

 print("¿Cual es el peso especifico de un cubo segun su peso y longitud de su arista (decimales detras de un punto)?")

 a = input("Arista del cubo en cm: ")
 a = strToFloat(a)
 peso = input("Su peso en kg: ")
 peso = strToFloat(peso)  

 peso = peso * 1000           #paso kg a gr
 volumen = pow(a,3)               #funcion para elevar a x potencia
 pesoEsp = peso / volumen       #funcion del peso especifico

 print("Su peso especifico sera de : ")
 print(pesoEsp, "g/cm²")
sys.exit()
