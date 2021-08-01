import os
from Calculadora import CalEstandar, CalCientifica
from Basico import Basico,Intermedio
from Lista import Lista
from Cadenas import Cadena

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
    men = Menu("Menú Principal",["1)Calculadora","2)Operación Números","3)Tratamiento de Listas","4)Operaciones de Cadenas","5)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 != "10":
            os.system("cls") 
            men1 = Menu("Menú Calculadora",["1)Suma","2)Resta","3)Multiplicación","4)División","5)Exponente","6)Valor Absoluto","7)Circunferencia","8)Área Circulo","9)Área Cuadrado","10)Salir"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("Suma de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print(("El resultado de {}+{}={}".format(n1,n2,cal.suma())))
                input("Presione una tecla para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Resta de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal= CalEstandar(n1,n2)
                print("El resultado de la resta {}-{}={}".format(n1,n2,cal.resta()))
                input("Presione una tecla para continuar")
            elif opc1 == "3":
                os.system("cls")
                print("Multiplicación de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de la multiplicacion {}*{}={}".format(n1,n2,cal.multiplicacion()))
                input("Presione una tecla para continuar")
            elif opc1 == "4":
                os.system("cls")
                print("Divison de dos numeros")
                n1 = int(input("ingrese numero1: "))
                n2 = int(input("ingrese numero2: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de la divison {}/{}={}".format(n1,n2,cal.division()))
                input("Presione una tecla para continuar")
            elif opc1 == "5":
                os.system("cls")
                print("Exponente de un numero")
                n1 = int(input("Ingrese base: "))
                n2 = int(input("Ingrese exponente: "))
                cal = CalEstandar(n1,n2)
                print("El resultado de {}**{}={}".format(n1,n2,cal.Exponente()))
                input("Presione una tecla para continuar")
            elif opc1 == "6":
                os.system("cls")
                print("Valor absoluto de un numero")
                numero = int(input("Ingrese un numero: "))
                cal = CalEstandar(0,0)
                print("El valor absoluto de {} es {}".format(numero, cal.valorAbsoluto(numero)))
                input("Presione una tecla para continuar")
            elif opc1 == "7":
                os.system("cls")
                print("La circunferencia del radio")
                radio = int(input("Ingrese el radio: "))
                cal = CalCientifica(0,0)
                print("La circunferencia del radio {} es {}".format(radio, cal.circunferencia(radio)))
                input("Presione una tecla para continuar")
            elif opc1 == "8":
                os.system("cls")
                print("El Area de un circulo")
                radio = int(input("Ingrese el radio: "))
                cal = CalCientifica(0,0)
                print("El area del circulo con el radio {} es {}".format(radio,cal.AreaCirculo(radio)))
                input("Presione una tecla para continuar")
            elif opc1 == "9":
                os.system("cls")
                print("El Area del cuadrado")
                lado = int(input("Ingrese el valor de un lado:"))
                cal = CalCientifica(0,0)
                print("El ara del cuadrado con los lados {} es {}".format(lado,cal.AreaCuadrado(lado)))
                input("Presione una tecla para continuar")
            elif opc1 == "10":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
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
                Bas = Basico
                Bas.numerosN(n1)
                input("Presione una tecla para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("Sumar los números de 1 a n")
                n1 = int(input("Ingrese número : "))
                Inter = Intermedio
                
                print("La suma de los número desde el 1 hasta el número {} es: {}".format(n1,Inter.numerosN(n1)))
                input("Presione una tecla para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("Múltiplo de cualquier número")
                n1 = int(input("Ingrese un número : "))
                n2 = int(input("Ingrese el multiplo del número :"))
                Bas = Basico
                res = Bas.Multiplo(n1,n2)
                if res == 0:
                    print("El número {} es multiplo de {}".format(n1,n2))
                else:
                    print("El número {} no es multiplo de {}".format(n1, n2))
                input("Presione una tecla para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("Presentar los divisores de un número")
                n1 = int(input("Ingrese número : "))
                Bas = Basico
                res =Bas.DivisoresNumero(n1)
                print("Los divisores del número {}, son: {}".format(n1,res))
                input("Presione una tecla para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("Número Primo")
                n1 = int(input("Ingrese número : "))
                Bas = Basico
                res = Bas.primo(n1)
                if res ==2:
                    print("El numero {}, es primo".format(n1))
                else:
                    print("El número {}, no es primo".format(n1))
                input("Presione una tecla para continuar")
            elif opc2 == "6":
                os.system("cls")
                print("Factorial de cualquier número")
                n1 = int(input("Ingrese un número : "))
                Inter = Intermedio
                res = Inter.factorial(n1)
                print("El factorial del número {} es: {}".format(n1,res))  
                input("Presione una tecla para continuar")
            elif opc2 == "7":
                os.system("cls")
                print("Fibonacci de una serie de n números")
                n1 = int(input("Ingrese la cantidad de numeros que desee que tenga la serie : "))
                Inter = Intermedio
                Inter.fibonacci(n1)
                input("\nPresione una tecla para continuar")
            elif opc2 == "8":
                os.system("cls")
                print("Perfecto")
                n1 = int(input("Ingrese un número : "))
                Bas = Basico
                res =Bas.perfecto(n1)
                if res ==n1:
                    print("El numero {}, es perfecto".format(n1))
                else:
                    print("El número {}, no es perfecto".format(n1))
                input("Presione una tecla para continuar")
            elif opc2 == "9":
                os.system("cls")
                print("Primos Gemelos")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                Inter = Intermedio
                res =Inter.primosGemelos(n1, n2)
                if res == (2, 2):
                    if n1 - n2 ==2 or n2 - n1 == 2:
                        print("Los números {} y {} son números primos gemelos".format(n1,n2))
                    else:
                        print("Los números {} y {} no son números primos gemelos".format(n1,n2))
                else:
                    print("Los números no son primos gemelos ya que uno de los dos número no es primo")
                input("Presione una tecla para continuar")
            elif opc2 == "10":
                os.system("cls")
                print("Números Amigos")
                n1 = int(input("Ingrese el número 1: "))
                n2 = int(input("Ingrese el número 2: "))
                Inter = Intermedio
                res =Inter.amigos(n1, n2)
                if res == (n2, n1):
                    print("Los números {} y {} son amigos".format(n1,n2))  
                else:
                    print("Los números {} y {} no son amigos".format(n1,n2))
                input("Presione una tecla para continuar")
            elif opc2 == "11":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")  
                input("Presione una tecla para continuar")
    elif opc == "3":
        opc3 =""
        while opc3 != "11":
            os.system("cls") 
            men3 = Menu("Menú Tratamiento de Listas",["1)Recorrer y presentar los datos de una lista","2)Buscar un valor en una lista","3)Retornar una lista con los factoriales","4)Retornar una lista de números primos","5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo ","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Recorrer y presentar los datos de una lista")
                print("Lista =",lista)
                Lis = Lista(lista)
                Lis.presentarLista()
                input("Presione una tecla para continuar")
            elif opc3 == "2":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Buscar un valor en una lista")
                print("Lista =",lista)
                Lis = Lista(lista)
                print(Lis.buscarLista())
                input("Presione una tecla para continuar")
            elif opc3 == "3":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Retornar una lista con los factoriales")
                print("Lista =",lista)
                Lis = Lista(lista)
                Lis.listaFactorial()
                input("Presione una tecla para continuar")
            elif opc3 == "4":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Retornar una lista de números primos")
                print("Lista =",lista)
                Lis = Lista(lista)
                resultado = Lis.listaPrimo()
                input("Presione una tecla para continuar")
            elif opc3 == "5":
                os.system("cls")
                print("Recorrer una lista de diccionario con notas de alumnos")
                li=[]
                di = {}
                cant = int(input('Ingrese el número de datos que va a tener el diccionario: '))
                for i in range(cant):
                    clave =input('Nombre del alumno: ')
                    valor =input('nota: ')
                    di[clave] = valor
                li.append(di)
                print(di)
                Lis = Lista(li)
                Lis.listaNotas(di)
                input("Presione una tecla para continuar")
            elif opc3 == "6":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Insertar un dato en una Lista dada lo Posición")
                print("Lista =",lista)
                valor = int(input("Ingrese valor a agregar: "))
                posicion = int(input("Ingrese posicion: "))
                Lis = Lista(lista)
                Lis.insertarLista(valor, posicion)
                input("Presione una tecla para continuar")
            elif opc3 == "7":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Eliminar todas las ocurrencias en una Lista")
                # INVOCAR
                input("Presione una tecla para continuar")
            elif opc3 == "8":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Retornar cualquier valor de una lista eliminándolo ")
                print("Lista =",lista)
                posicion = int(input("Eliminar posicion: "))
                Lis = Lista(lista)
                print("El número que se encontraba en la posicion {} es {} y la lista quedo de la siguiente forma {} ".format(posicion,lista[posicion],Lis.retornaValorLista(posicion)))
                input("Presione una tecla para continuar")
            elif opc3 == "9":
                os.system("cls")
                print("Copiar cada elemento de una tupla en una lista")
                tupla,cont = (), 0
                nun = int(input("Ingrese el número de datos que desea que tenga la tupla: "))
                while cont != nun:
                    valor = str(input("Ingrese el valor que desea que este en la tupla: "))
                    tupla = tupla + (valor,)
                    cont +=1
                print("Tupla: ",tupla)
                Lis = Lista("NADA")
                print("Lista: ",Lis.copiarTuplaLista(tupla))
                input("Presione una tecla para continuar")
            elif opc3 == "10":
                os.system("cls")
                print("Dar el vuelto a varios clientes")
                li=[]
                di = {}
                cant = int(input('Ingrese el número de datos que va a tener el diccionario: '))
                for i in range(cant):
                    clave =input('Nombre del cliente: ')
                    valor =input('vuelto $: ')
                    di[clave] = valor
                li.append(di)
                print(di)
                Lis = Lista(li)
                Lis.vueltoLista(di)
                input("Presione una tecla para continuar")
            elif opc3 == "11":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
    elif opc == "4":
        opc4 =""
        while opc4 != "10":
            os.system("cls") 
            men4 = Menu("Menú Operaciones de Cadenas",["1)Recorrer y presentar los datos de una cadena","2)Buscar un carácter en una cadena","3)Retornar una lista con la posiciones dado un carácter de la cadena","4)Retornar una lista con todas las palabras de una cadena","5)Retornar una cadena a partir de una lista","6)Insertar un dato en una cadena dada lo Posición","7)Eliminar todas las ocurrencias en una cadena","8)Retornar cualquier valor de una cadena eliminándolo ","9)Concatenar cadenas","10)Salir"])
            opc4 = men4.menu()
            if opc4 == "1":
                os.system("cls")
                print("Recorrer y presentar los datos de una cadena")
                cadena = str(input("Ingrese una palabra o oración: "))
                Cad = Cadena(cadena)
                Cad.recorrerCadena()
                input("Presione una tecla para continuar")
            elif opc4 == "2":
                os.system("cls")
                print("Buscar un carácter en una cadena")
                cadena = str(input("Ingrese una palabra o oración: "))
                buscar = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.buscarCaracter(buscar))
                input("Presione una tecla para continuar")
            elif opc4 == "3":
                os.system("cls")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                cadena = str(input("Ingrese una palabra o oración: "))
                caracter = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.listaPosiciones(caracter))
                input("Presione una tecla para continuar")
            elif opc4 == "4":
                os.system("cls")
                print("Retornar una lista con todas las palabras de una cadena")
                cadena = str(input("Ingrese una palabra o oración: "))
                Cad = Cadena(cadena)
                print(Cad.listaPalabras())
                input("Presione una tecla para continuar")
            elif opc4 == "5":
                os.system("cls")
                print("Retornar una cadena a partir de una lista")
                lista =[]
                cont =0
                x =int(input("Ingrese la cantidad que desea que tenga la lista: "))
                while x != cont:
                    y = input("Ingrese los datos para la lista: ")
                    lista.append(y)
                    cont +=1
                print("Lista: ",lista)
                Cad = Cadena("NADA")
                print("Cadena: ",Cad.cadenaLista(lista))
                input("Presione una tecla para continuar")
            elif opc4 == "6":
                os.system("cls")
                print("Insertar un dato en una cadena dada lo Posición")
                cadena = str(input("Ingrese una palabra o oración: "))
                dato = input("Ingrese el dato que va a ingresar a la cadena: ")
                posicion = int(input("Ingrese la posicion donde va a colocar el dato: "))
                Cad = Cadena(cadena)
                print(Cad.insertarDato(dato, posicion))
                input("Presione una tecla para continuar")
            elif opc4 == "7":
                os.system("cls")
                print("Eliminar todas las ocurrencias en una cadena")
                cadena = str(input("Ingrese una palabra o oración: "))
                buscar = str(input("Ingrese la ocurrencia que desea eliminar: "))
                Cad = Cadena(cadena)
                print(Cad.eliminarOcurrencias(buscar))
                input("Presione una tecla para continuar")
            elif opc4 == "8":
                os.system("cls")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                cadena = str(input("Ingrese una palabra o oración: "))
                posicion = int(input("Ingrese la posición donde se encuntre el caracter: "))
                Cad = Cadena(cadena)
                print(Cad.retornaValor(posicion))
                input("Presione una tecla para continuar")
            elif opc4 == "9":
                os.system("cls")
                print("Concatenar cadenas")
                cadena = str(input("Ingrese una palabra o oración: "))
                dato = str(input("Ingrese lo que va a concatenar a la cadena: "))
                Cad = Cadena(cadena)
                print(Cad.concatenarCadena(dato))
                input("Presione una tecla para continuar")
            elif opc4 == "10":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
    elif opc == "5":
        print("Lo esperamos en una proxima ocasión")
    else:
        print("Opción no valida")
        input("Presione una tecla para continuar")