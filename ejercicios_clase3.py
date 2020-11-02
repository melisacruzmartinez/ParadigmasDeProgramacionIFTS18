import time
## Se hablo de la eficacia y eficiencia en codear. 
## Hasta hoy se realizo todo con eficacia. Hoy empezaremos con eficiciencia.
## Aprender a resolver ejercicios de la mejor manera !

## Ejercicios con gaus  " s = (n/2)*(n+1) "

## Metodo tradicional

#def suma_lineal():
 #   suma = 0
  #  for numero in range (1,100):
   #     suma += numero
    #return suma

#def suma_continua():
 #   return (100/2) * (100+1)

#print (suma_lineal)
#print (suma_continua)

##___________________________________________________________________

##Ejemplo mejorado con time podemos medir el tiempo que tarda en recorrer
## Es importante saber cual de los dos metodos tarda menos tiempo
## la segunda funcion al principio tarda más pero a la larga se matiene constante

def suma_lineal(cant):
    suma=0
    for numero in range(1,cant +1):
        suma += numero
        return suma

def suma_continua (cant):
    return(cant/2) * (cant + 1)

cantidad = 1000000

for i in range(4):

    t_0 = time.time()
    suma1 = suma_lineal(cantidad)

    t_1 = time.time()
    suma2 = suma_continua(cantidad)

    t_2 = time.time()

    print(f"{suma1}, {t_1 - t_0}")
    print(f"{suma2}, {t_2 - t_1}")

    cantidad*=10