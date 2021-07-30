from basico import Intermedio

class Lista(Intermedio):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista

    # 5)Recorrer una lista de diccionario con notas de alumnos
    def listaNotas(self, listaDiccionarioNotas):
        for clave, valor in listaDiccionarioNotas.items():
            print(clave, ':', valor)

    # 6) Insertar un dato en una Lista dada lo Posición
    def insertarLista(self, valor, posicion):
        self.lista.insert(posicion, valor)
        print(self.lista)

     # 7)Eliminar todas las ocurrencias en una Lista
    def eliminarLista(self):
        nuevaLista = []
        for valor in self.lista:
            if valor not in nuevaLista:
                nuevaLista.append(valor)
        print("lista sin ocurrencias: {}".format(nuevaLista))

    # 8)Retornar cualquier valor de una lista eliminándolo
    def retornaValorLista(self, posicion):
        del self.lista[posicion]
        return self.lista
    
    # 9) Copiar Tupla Lista
    def copiarTuplaLista(self):
        print(" Copiar cada elemento de una tupla en una lista ")
        aux1=list(self.tupla)
        return aux1      

    
    # 10) Dar el vuelto a varios clientes
    def vueltoLista(self, listaClientesDiccionario):
        pass


'''creando instancia de clase'''
lis = Lista([1,4,4,5,6,6,8,2,13])

'''Presentaciones de metodos'''


# valor = input("Ingrese valor a agregar: ")
# posicion = int(input("Ingrese posicion: "))
# lis.insertarLista(valor, posicion)

# lis.eliminarLista()

# posicion = int(input("Eliminar posicion: "))
# print(lis.retornaValorLista(posicion))

# ----falta metodo5 ----
# ----falta metodo10 ----