class Basico:

    def numerosN(n):  # PRESENTAR LOS NUMEROS DEL 1 AL N
        cont = 0
        while n != cont :
            cont += 1
            print(cont)
                   
    def Multiplo(numero, multiplo):  # MULTIPLO DE CUALQUIER NUMERO
        res = numero % multiplo
        return res
           
    def DivisoresNumero(numero):  # PRESENTAR LOS DIVISORES DE UN NUMERO
        cont = 1
        divisores = []
        while  numero != cont :
            reci = numero % cont
            if reci == 0:
                divisores.append(cont)
            cont += 1
        return divisores

    def primo(numero):    # NUMERO PRIMO
        cont = 1
        resi = 0
        while numero >= cont:
            if numero % cont == 0:
                resi += 1
            cont +=1   
        return resi
    
    def perfecto(numero):    # PERFECTO
        cont = 1
        divi = 0
        while numero > cont:
            if numero % cont == 0:
                divi += cont
            cont +=1
        return divi

class Intermedio(Basico):

    def numerosN(n):   # APLICAR POLIMORFISMO   # SUMAR LOS NUMEROS DEL 1 AL N
        cont = 1
        suma = 0
        while n >= cont :
            suma = suma + cont
            cont += 1
        return suma

    def factorial(numero):  # FACTORIAL DE CUALQUIER NUMERO
        cont, multi = 1,1
        while numero >= cont:
            multi = multi * cont
            cont +=1
        
        return multi
        
    def fibonacci(n):  #FIBONACCI DE UNA SERIE DE N NUMEROS
        cont,x,y  =1, 1, 1
        print("La serie de Fibonacci de {} números es:".format(n))
        while cont < n:
            print(x, end = ", ")
            x,y=y, x+y
            cont +=1
        print(x, end = "")
    
    def primosGemelos(nun1, nun2):    # PRIMOS GEMELOS
        res = Basico
        resultado1 =res.primo(nun1)
        resultado2 =res.primo(nun2)
        return resultado1, resultado2

    def amigos(nun1, nun2):   # NUMEROS AMIGOS
        cont1, cont2 = 0,0
        res = Basico
        resultado1 = res.DivisoresNumero(nun1)
        resultado2 = res.DivisoresNumero(nun2)
        for res1 in range(len(resultado1)):
            cont1 = cont1 + resultado1[res1]
        for res2 in range(len(resultado2)):
            cont2 = cont2 +resultado2[res2]
        return cont1, cont2 

# nun = 6
# multiplo = 2
# nun1 = 31
# nun2 =29
# Bas = Basico
#Bas.numerosN(nun)      ###### TERMINADO
# res =(Bas.Multiplo(nun, multiplo))        ###### TERMINADO
# if res == 0:
#     print("El número {} es multiplo de {}".format(nun,multiplo))
# else:
#     print("El número {} no es multiplo de {}".format(nun, multiplo))

# res =Bas.DivisoresNumero(nun)   ##### TERMINADO
# print("Los divisores del número {}, son: {}".format(nun,res))

# res =Bas.primo(nun)          ###### TERMINADO
# if res ==2:
#     print("El numero {}, es primo".format(nun))
# else:
#     print("El número {}, no es primo".format(nun))

# res =Bas.perfecto(nun)         ###### TERMINADO
# if res ==nun:
#     print("El numero {}, es perfecto".format(nun))
# else:
#     print("El número {}, no es perfecto".format(nun))

# Inter = Intermedio
# print("La suma de los número desde el 1 hasta el número {} es: {}".format(nun,Inter.numerosN(nun)))     ####### TERMINADO

# print("El factorial del número {} es: {}".format(nun,Inter.factorial(nun)))       ####### TERMINADO

# Inter.fibonacci(nun)      ####### TERMINADO

# res =Inter.primosGemelos(nun1,nun2)   ###### TERMINADO
# if res == (2, 2):
#     if nun1 - nun2 ==2 or nun2 - nun1 == 2:
#         print("Los números {} y {} son números primos gemelos".format(nun1,nun2))
#     else:
#         print("Los números {} y {} no son números primos gemelos".format(nun1,nun2))
# else:
#     print("Los números no son primos gemelos ya que uno de los dos número no es primo")

# res =Inter.amigos(nun1, nun2)       ###### TERMINADO   1210,1184
# if res == (nun2, nun1):
#     print("Los números {} y {} son amigos".format(nun1,nun2))  
# else:
#     print("Los números {} y {} no son amigos".format(nun1,nun2))