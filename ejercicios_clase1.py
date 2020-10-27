#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
#
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.
def exercise1():
    menssage = "Hello World!"
    print (menssage)
#exercise1()
# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.
def excercise2():
    for number in range (0,101):
        if number % 2 == 0:
            print(number)
#excercise2()

# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.
def excercise3():
    for number in range (0,101):
        if number % 3 == 0:
            print(number)
#excercise3()

# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.
def excercise4():
    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))
    sum = number1 + number2
    sub = number1 - number2
    div = number1 / number2
    mult = number1 * number2

    print ("Chosen numbers",number1," and ",number2)
    print ("Addition = ", sum)
    print ("Substraction = ",sub )
    print ("Multiplication = ", mult)
    print ("Division = ", div)
#excercise4()

# Ejercicio 5
#
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.
def excercise5():
    userValueList = []
    for number in range(10):
        userValue = int(input("Enter number int : "))
        userValueList.append(userValue)

    print(userValueList)
    userValueList.sort()
    print(userValueList)
#excercise5()

# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.
def excercise6(number1, number2):
    if number1 > number2:
        return 1
    elif number1 == number2:
        return 0
    else:
        return -1

#userInput1 = int(input("Enter number int1 : "))
#userInput2 = int(input("Enter number int2 : "))
87
#resultado = excercise6(userInput1, userInput2)
#print(resultado)

# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
def excercise7(number1, number2):
    midle = (number1 + number2) / 2
    return midle 
#userInput1 = int(input("Enter number int1 : "))
#userInput2 = int(input("Enter number int2 : "))

#resultado = excercise7(userInput1, userInput2)
#print(resultado)
#
# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#
def excercise8():
    userValueList = [4,5,2,22,11,78,45,9,7,10]
    list1 = []
    list2 = []
    for i in range (len(userValueList)):
        if userValueList[i] % 2 == 0:
            list1.append(userValueList[i])
        else: 
            list2.append(userValueList[i])
    list1.sort()
    list2.sort()
    print (list1,list2)
    return list1,list2   
#excercise8()
# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".
def excercise9(mail):
    if "@" in mail:
        print ("User ok")
    else :
        print ("User invalid")

#userInput = str(input("Enter mail : "))
#excercise9(userInput)
# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def excercise10(dni):
    sum = 0
    for i in dni:
        sum = sum +1
    if 7<=sum<=8:
        print ("Number ok")
        return True
    else :
        print ("Number invalid")
        return False

#userInput = str(input("Enter DNI : "))
#excercise10(userInput)
1
# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
def excercise11(userInput):
    wordList = userInput.split()
    return len(wordList[-1])
#result = excercise11("Bienvenidos a paradigmas de programación")
#print(result)

# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#
def excercise12(nuggets):
    if nuggets == 6 or nuggets == 9 or nuggets == 20 :
        print ("Okey, wait a moment please")
    else :
        print ("sorry, it´s not possible")
menu = int(input(" Have you decided how much nuggets need ? : "))
excercise12(menu)