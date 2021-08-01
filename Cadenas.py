class Cadena:
    def __init__(self, cadena):
        self.cadena=cadena
        
    def  recorrerCadena(self):
        cont = 0
        for i, caracter in enumerate(self.cadena):
            cont += 1
            print("Caracter {}: {} ".format(cont,caracter))

    def  buscarCaracter(self,buscado):
        x = self.cadena.find(buscado)
        if x != -1:
            return x
        else:
            return "error"
        
    def  listaPosiciones(self,caracter):  # RETORNAR UNA LISTA CON LA POSICIONES DADO UN CARACTER DE LA CADENA
        res = []
        for pos1 in range(len(self.cadena)):
            for pos2 in range(len(caracter)):
                if self.cadena[pos1] == caracter[pos2]:
                    res.append(pos1)
        return res

    def listaPalabras(self):   #TERMINADA
        lista = self.cadena.split()
        return lista

    def cadenaLista(self,lista):  #TERMINADO
        return " ".join(map(str,lista))

    def insertarDato(self,buscado,posicion):   #TERMINADA
        lista = self.cadena.split()
        lista.insert(posicion,buscado)
        lista1 = Cad.cadenaLista(lista)
        return lista1

    def eliminarOcurrencias(self,buscado):   #TERMINADA
        if buscado == str(buscado):
            elim = self.cadena.split(buscado)
            modificado = Cad.cadenaLista(elim)
            return modificado
        if buscado == int(buscado):
            x = self.cadena[:buscado] + self.cadena[buscado+1:]
            modificado = Cad.cadenaLista(x)
            return modificado

    def retornaValor(self, posicion):  # posicion    #TERMINADA

        lista = list(self.cadena)
        aux = lista[posicion]
        x = self.cadena.replace(aux,"")
        return aux,x

    def concatenarCadena(self,dato):   #TERMINADA
        self.cadena = self.cadena + " "
        return self.cadena + dato

cadena = "Lo unico imposible es aquello que no intentas."
Cad = Cadena(cadena)
#----------------------1
#Cad.recorrerCadena()
#----------------------2
#buscar = "e"
#print(Cad.buscarCaracter(buscar))
#----------------------3
#caracter = "e"
#print(Cad.listaPosiciones(caracter))
#----------------------4
#print(Cad.listaPalabras())
#----------------------5
lista =[1,2,3,4,5,6]
print(Cad.cadenaLista(lista))
#----------------------6
#buscado = "oso"
#posicion = 2
#print(Cad.insertarDato(buscado,posicion))
#----------------------7
#buscado = "a"
#print(Cad.eliminarOcurrencias(buscado))
#----------------------8
#posicion = 17
#print(Cad.retornaValor(posicion))
#-----------------------9
#dato = "Ya que si te das por vencido nunca lo lograras"
#print(Cad.concatenarCadena(dato))