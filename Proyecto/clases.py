from MyLista import *

class Matriz:

    def __init__(self):
        self.nombre = ListaCircular()
        self.fila = ListaCircular()
        self.columna = ListaCircular()
        self.dato = ListaCircular()

    def guardar(self, nombre, n, m, dato):
        self.nombre.add(nombre)
        self.fila.add(n)
        self.columna.add(m)
        self.dato.add(dato)

    def crearMatrizPatrones(self):
        matriz_patrone = ListaCircular()
        lista = ListaCircular()
        listaJ = ListaCircular()
        listaK = ListaCircular()
        for i in range(len(self.dato)):
            lista = self.dato.index(i).value
            fila = ListaCircular()
            for j in range(len(lista)):
                listaJ = lista.index(j).value
                columna = ListaCircular()
                for k in range(len(listaJ)):
                    listaK = listaJ.index(k).value
                    if listaK.value > 0:
                        columna.add(1)
                    else:
                        columna.add(0)
                fila.add(columna)
            matriz_patrone.add(fila)
        return matriz_patrone

    def grupos_Matriz(self, matriz):
        unico = ListaCircular()
        for x in range(len(matriz)):
            fila_binaria = matriz.index(x).value
            if unico.buscar(str(fila_binaria)) == False:
                unico.add(str(fila_binaria))
        grupos = ListaCircular()
        for i in range(len(unico)):
            contador = 0
            repetidos = ListaCircular()
            for j in range(len(matriz)):
                if str(unico.index(i)) == str(matriz.index(j)):
                    repetidos.add(contador)
                contador += 1
            grupos.add(repetidos)
        return grupos

class Matriz_Reducida:

    def __init__(self):
        self.nombre = ListaCircular()
        self.fila = ListaCircular()
        self.columna = ListaCircular()
        self.grupos = ListaCircular()
        self.frecuencia = ListaCircular()
        self.no_frecuencia = ListaCircular()
        self.matriz = ListaCircular()

    def guardar(self, nombre, n, m, g, f, no_f, matriz):
        self.nombre.add(nombre)
        self.fila.add(n)
        self.columna.add(m)
        self.grupos.add(g)
        self.frecuencia.add(f)
        self.no_frecuencia.add(no_f)
        self.matriz.add(matriz)