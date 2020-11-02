## Forma avanzada de listas. (simplificacion) es útil en algunas situaciones. 

## ejemplo 1
# lista = []
# for numero in range(0,11):
#     lista.append(numero ** 2)
# print(lista)
#___________________________
# lista_c = [numero **2 for numero in range(0,11)]
# print(lista_c)


## ejemplo 2
#lista = []
#for numero in range(0,11):
 #   if numero % 2 == 0:
 #       lista.append(numero ** 2)
#print(lista)

#___________________________

#lista_c = [numero **2 for numero in range(0,11) if numero % 2 == 0]
#print(lista_c)

##___________________________________________________________________________________________________________________

## Lambda funciones anónimas. ( en este caso no nombramos funciones y podemos utilizarlas igual. Tener mucho cuidado donde se usan)
## tienen que entrar en lo posible en 1 sola línea de código y debería se usada cuando no se debe llamar la función mas de 1 vez

#numeros = [2, 5, 10, 23, 50, 33]
#
# def multiple(numeros):
#     if numeros % 5 == 0:
#         return True

# resultado = list(filter(multiple, numeros))

#resultado2 = list(filter(lambda numero: numero % 5 == 0, numeros))

#print(resultado, resultado2)

#____________________________

# def doblar(numero):
#     resultado = numero * 2
#     return resultado
#
# print(doblar(2))
##___________________________

# simplificando paso 1
# def doblar(numero):
#     return numero *2
#
# print(doblar(2))

##____________________________

#doblar = lambda  numero: numero *2

#print(doblar(2))

##___________________________________________________________________________________________________

## Uso del map ! Se usa como iterable 

#numeros = [2, 5, 10, 23, 50, 33]

#
# def doblar(numero):
#     return numero *2
#
#
# print(list(map(doblar, numeros)))

#_________________________________

#print(list(map(lambda numero: numero *2, numeros)))

##___________________________________________________________________________________________________

## Recursividad ! no es exactamente circular es mas bien como un remolino. Tiene un inicio y un fin pero podria llegar a estirarse mucho.
## Ejemplo mas común sacar factorial de un número.

# 5! = 5 * 4! = 120
# 4! = 4 * 3! =  24
# 3! = 3 * 2! =  6
# 2! = 2 * 1! = 2
# 1! = 1 * 0! = 1
# 0! = 1 = 1

# % * 4 * 3 * 2 * 1

def factorial(numero):
    if numero == 0:
        return 1
    else:
        print(f"soy el {numero}")
        # recur = factorial(numero -1)
        # da = recur * numero
        # return da

        return factorial(numero -1) * numero


#print(factorial(5))

## Ejemplo con fibonacci

def sacarFibonacci(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return sacarFibonacci(numero -1) + sacarFibonacci(numero - 2)

print(sacarFibonacci(10))