import os
from basico import Basico,Intermedio
from calculadora import calEstandar,calCientifica
from Tratamientolistas import Lista

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion [1....{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menú Principal",["1)Calculadora","2)Operació Números","3)Tratamiento de Listas","4)Operaciones de Cadenas","5)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 != "10":
            os.system("cls") 
            men1 = Menu("Menú Calculadora",["1)Suma","2)Resta","3)Multiplicación","4)División","5)Exponente","6)Valor Absoluto","7)Circunferencia","8)Área Circulo","9)Área Cuadrado","10)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("Suma de dos Números")
                n1 = int(input("Ingrese número 1: "))
                n2 = int(input("Ingrese número 2: "))
                #cal = calEstandar(n1,n2)
                #print(cal.suma())
                input("Presione una tecla para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Resta de dos Números")
                n1 = int(input("Ingrese número 1: "))
                n2 = int(input("Ingrese número 2: "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "3":
                os.system("cls")
                print("Multiplicación de dos Números")
                n1 = int(input("Ingrese número 1: "))
                n2 = int(input("Ingrese número 2: "))
                #cal = calEstandar(n1,n2)
                #print("{}*{}={}".format(n1,n2,cal.mutiplicacion()))
                input("Presione una tecla para continuar")
            elif opc1 == "4":
                os.system("cls")
                print("División entre dos Números")
                n1 = int(input("Ingrese número 1: "))
                n2 = int(input("Ingrese número 2: "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "5":
                os.system("cls")
                print("Base y Exponente")
                n1 = int(input("Ingrese número 1: "))
                n2 = int(input("Ingrese número 2: "))
                #INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "6":
                os.system("cls")
                print("Valor Absoluto")
                n1 = int(input("Ingrese un número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "7":
                os.system("cls")
                print("Circunferencia")
                n1 = int(input("Ingrese el radio: "))
                #INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "8":
                os.system("cls")
                print("Área de un Circulo")
                n1 = int(input("Ingrese el radio: "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc1 == "9":
                os.system("cls")
                print("Área de un Cuadrado")
                n1 = int(input("Ingrese el valor del lado a: "))
                n2 = int(input("Ingrese el valor del lado b: "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc == "10":
                print("Gracias por usar el sistema")
            else:
                print("Opción no valida")
    elif opc == "2":
        opc2 =""
        while opc2 != "11":
            os.system("cls") 
            men2 = Menu("Menú Operación Número",["1)Presentar los números de 1 a n","2)Sumar los números de 1 a n","3)Multiplo de cualquier número","4)Presentar los divisores de un número","5)Número Primo","6)Factorial de cualquier número","7)Fibonacci de una serie de números","8)Perfecto","9)Primos Gemelos","10)Números Amigos","11)Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("Presentar los números de 1 a n")
                n1 = int(input("Ingrese número : "))
                Bas = Basico(n1)
                Bas.numerosN()
                input("Presione una tecla para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("Sumar los números de 1 a n")
                n1 = int(input("Ingrese número : "))
                Inter = Intermedio(n1)
                Inter.numerosN()
                input("Presione una tecla para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("Múltiplo de cualquier número")
                n1 = int(input("Ingrese número : "))
                Bas = Basico(n1)
                Bas.Multiplo()
                input("Presione una tecla para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("Presentar los divisores de un número")
                n1 = int(input("Ingrese número : "))
                Bas = Basico(n1)
                Bas.DivisoresNumero()
                input("Presione una tecla para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("Número Primo")
                n1 = int(input("Ingrese número : "))
                Bas = Basico(n1)
                Bas.primo()
                input("Presione una tecla para continuar")
            elif opc2 == "6":
                os.system("cls")
                print("Factorial de cualquier número")
                n1 = int(input("Ingrese un número : "))
                Inter = Intermedio(n1)
                Inter.factorial()
                input("Presione una tecla para continuar")
            elif opc2 == "7":
                os.system("cls")
                print("Fibonacci de una serie de n números")
                n1 = int(input("Ingrese la cantidad de numeros que desee que tenga la serie : "))
                Inter = Intermedio(n1)
                Inter.fibonacci()
                input("\nPresione una tecla para continuar")
            elif opc2 == "8":
                os.system("cls")
                print("Perfecto")
                n1 = int(input("Ingrese un número : "))
                Bas = Basico(n1)
                Bas.perfecto()
                input("Presione una tecla para continuar")
            elif opc2 == "9":
                os.system("cls")
                print("Primos Gemelos")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                Inter = Intermedio(n1, n2)
                Inter.primosGemelos()
                input("Presione una tecla para continuar")
            elif opc2 == "10":
                os.system("cls")
                print("Números Amigos")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                Inter = Intermedio(n1, n2)
                Inter.amigos()
                input("Presione una tecla para continuar")
            elif opc == "11":
                print("Gracias por usar el sistema")
            else:
                print("Opción no valida")  
    elif opc == "3":
        opc3 =""
        while opc3 != "11":
            os.system("cls") 
            men3 = Menu("Menú Tratamiento de Listas",["1)Recorrer y presentar los datos de una lista","2)Buscar un valor en una lista","3)Retornar una lista con los factoriales","4)Retornar una lista de números primos","5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo ","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
            opc3 = men3.menu()

            lista = []
            cantidad = int(input("Cuantos elementos desea ingresar a la lista: "))
            for i in range(cantidad):
                val = input("Ingrese elemento a la lista:")
                lista.append(val)
                lis = Lista(lista)

            if opc3 == "1":
                os.system("cls")
                print("Recorrer y presentar los datos de una lista")
                n1 = int(input("Ingrese número : "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "2":
                os.system("cls")
                print("Buscar un valor en una lista")
                n1 = int(input("Ingrese número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "3":
                os.system("cls")
                print("Retornar una lista con los factoriales")
                n1 = int(input("Ingrese número : "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "4":
                os.system("cls")
                print("Retornar una lista de números primos")
                n1 = int(input("Ingrese número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "5":
                os.system("cls")
                print("Recorrer una lista de diccionario con notas de alumnos")
                n1 = int(input("Ingrese número : "))
                #INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "6":
                os.system("cls")
                print('Lista:',lista)
                print("Insertar un dato en una Lista dada lo Posición")
                valor = input("Ingrese valor a agregar: ")
                posicion = int(input("Ingrese posicion: "))
                lis.insertarLista(valor, posicion)
                input("Presione una tecla para continuar")
            elif opc3 == "7":
                os.system("cls")
                print('Lista:',lista)
                print("Eliminar todas las ocurrencias en una Lista")
                lis.eliminarLista()
                input("Presione una tecla para continuar")
            elif opc3 == "8":
                os.system("cls")
                print('Lista:',lista)
                print("Retornar cualquier valor de una lista eliminándolo ")
                posicion = int(input("Eliminar posicion: "))
                print(lis.retornaValorLista(posicion))
                input("Presione una tecla para continuar")
            elif opc3 == "9":
                os.system("cls")
                print("Copiar cada elemento de una tupla en una lista")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "10":
                os.system("cls")
                print("Dar el vuelto a varios clientes")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc == "11":
                print("Gracias por usar el sistema")
            else:
                print("Opción no valida")     
    elif opc == "4":
        opc4 =""
        while opc4 != "10":
            os.system("cls") 
            men4 = Menu("Menú Operaciones de Cadenas",["1)Recorrer y presentar los datos de una cadena","2)Buscar un carácter en una cadena","3)Retornar una lista con la posiciones dado un carácter de la cadena","4)Retornar una lista con todas las palabras de una cadena","5)Retornar una cadena a partir de una lista","6)Insertar un dato en una cadena dada lo Posición","7)Eliminar todas las ocurrencias en una cadena","8)Retornar cualquier valor de una cadena eliminándolo ","9)Concatenar cadenas","10)Salir"])
            opc4 = men4.menu()
            if opc4 == "1":
                os.system("cls")
                print("Recorrer y presentar los datos de una cadena")
                n1 = int(input("Ingrese número : "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "2":
                os.system("cls")
                print("Buscar un carácter en una cadena")
                n1 = int(input("Ingrese número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "3":
                os.system("cls")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                n1 = int(input("Ingrese número : "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "4":
                os.system("cls")
                print("Retornar una lista con todas las palabras de una cadena")
                n1 = int(input("Ingrese número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "5":
                os.system("cls")
                print("Retornar una cadena a partir de una lista")
                n1 = int(input("Ingrese número : "))
                #INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "6":
                os.system("cls")
                print("Insertar un dato en una cadena dada lo Posición")
                n1 = int(input("Ingrese un número : "))
                ## INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "7":
                os.system("cls")
                print("Eliminar todas las ocurrencias en una cadena")
                n1 = int(input("Ingrese la cantidad de numeros que desee que tenga la serie : "))
                #INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "8":
                os.system("cls")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                n1 = int(input("Ingrese un número : "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "9":
                os.system("cls")
                print("Concatenar cadenas")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc4 == "10":
                print("Gracias por usar el sistema")
            else:
                print("Opción no valida")