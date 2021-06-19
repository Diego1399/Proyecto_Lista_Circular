import xml.etree.ElementTree as ET
from graphviz import Digraph
from clases import *
from MyLista import *
import time

Menu_principal = {'1', '2', '3', '4', '5', '6'}

matriz = Matriz() # Guarda la matriz y sus datos generales como el nombre, la cantidad de filas y la cantidad de columnas
matriz_obtenida = Matriz_Reducida()

while True:
    print('''   
Menú principal:
    1. Cargar archivo
    2. Procesar archivo
    3. Escribir archivo salida
    4. Mostrar datos del estudiante
    5. Generar gráfica
    6. Salida
''')

    opcion = input('Seleccione una opcion: ')

    if not (opcion in Menu_principal):
        print('Opcion no valida')
        continue

    if opcion == '1':
        time.sleep(0.1)
        print('\nOpcion Cargar Archivo:')
        archivo = input('Ingrese la ruta del archivo: ')
        try:
            archivo_xml = ET.parse(archivo) # Vusca y lee ek archivo XML a partir de la ruta ingresada
            raiz = archivo_xml.getroot()
            # se recorre el archivo mediante las etiquetas que contiene
            for dato_matiz in raiz:
                nombre = dato_matiz.attrib['nombre']

                fila = dato_matiz.attrib['n']

                columna = dato_matiz.attrib['m']

                mayor_x = 0
                mayor_y = 0

                lista_x = []
                lista_y = []

                lista_dato = ListaCircular()

                for index in dato_matiz:
                    x_actual = int(index.attrib['x'])
                    if x_actual > mayor_x:
                        mayor_x = x_actual
                    else:
                        mayor_x = mayor_x
                    y_actual = int(index.attrib['y'])
                    if y_actual > mayor_y:
                        mayor_y = y_actual
                    else:
                        mayor_y = mayor_y

                    lista_x.append(x_actual)
                    lista_y.append(y_actual)

                    lista_dato.add(int(index.text))

                contador = 0

                matriz_operar = ListaCircular() # variable que almacena los datos de la matriz del XML

                for no_fila in range(0, int(fila)):
                    fila_matriz = ListaCircular()
                    for no_columna in range(0, int(columna)):
                        fila_matriz.add(lista_dato.index(contador))
                        contador += 1
                    matriz_operar.add(fila_matriz)

                if int(fila) == int(mayor_x) and int(columna) == int(mayor_y) and len(lista_x) == len(lista_y):
                    matriz.guardar(nombre, fila, columna, matriz_operar)

        except:
            print('Ocurrio un error')

        continue

    if opcion == '2':
        time.sleep(0.1)
        print('\nProcesar archivo')

        print('> Calculando la matriz binaria...')
        time.sleep(3)

        grupos_matriz = ListaCircular()

        lista_index = ListaCircular()

        matrizBinaria = matriz.crearMatrizPatrones()

        for i in range(len(matrizBinaria)):
            lista_index = matrizBinaria.index(i).value
            matriz.grupos_Matriz(lista_index)
            grupos_matriz.add(matriz.grupos_Matriz(lista_index))

        print('> Realizando suma de tuplas...')
        time.sleep(3)
        contador = 0
        index_lista = ListaCircular()
        for lista_index in range(len(grupos_matriz)):

            lista = matriz.dato.index(lista_index).value

            index_lista = grupos_matriz.index(lista_index).value

            reducida = ListaCircular()
            frecuencia = ListaCircular()
            no_fercuencia = ListaCircular()

            m = 0
            for index in range(len(index_lista)):
                no_fercuencia.add(len(index_lista.index(index).value))
                posicion = ListaCircular()
                if len(index_lista.index(index).value) > 1:
                    auxiliar = ListaCircular()
                    posicion = index_lista.index(index).value
                    for x in range(len(posicion)):
                        m = len(lista.index(posicion.index(x).value).value)
                        if len(auxiliar) == 0:
                            auxiliar = lista.index(posicion.index(x).value).value
                            frecuencia.add(posicion.index(x).value + 1)
                        else:
                            respuesta = ListaCircular()
                            for y in range(len(auxiliar)):
                                valor1 = auxiliar.index(y).value
                                valor2 = lista.index(posicion.index(x).value).value.index(y).value
                                respuesta.add(valor1.value + valor2.value)
                            reducida.add(respuesta)
                else:
                    posicion = index_lista.index(index).value
                    for x in range(len(posicion)):
                        m = len(lista.index(posicion.index(x).value).value)
                        frecuencia.add(posicion.index(x).value + 1)
                        reducida.add(lista.index(posicion.index(x).value).value)

            nombre = matriz.nombre.index(contador)
            n = len(reducida)
            g = len(reducida)
            matriz_obtenida.guardar(nombre, n, m, g, frecuencia, no_fercuencia, reducida)
            contador += 1
        continue

    if opcion == '3':
        time.sleep(0.1)
        print('\n')
        ruta_especifica = input('Escribir una ruta especifica: ')
        try:
            print('Se escribio el archivo satisfactorio')

            root = ET.Element("matrices")
            for i in range(len(matriz_obtenida.nombre)):
                nombre = matriz_obtenida.nombre.index(i).value
                n = matriz_obtenida.fila.index(i).value
                m = matriz_obtenida.columna.index(i).value
                g = matriz_obtenida.grupos.index(i).value
                frecuencia = matriz_obtenida.frecuencia.index(i).value
                g_frecuencia = matriz_obtenida.no_frecuencia.index(i).value

                nombre_Salida = str(nombre) + "_Salida"

                doc = ET.SubElement(root, "matriz", nombre=nombre_Salida, n=str(n), m=str(m), g=str(g))

                matriz_Salida = matriz_obtenida.matriz.index(i).value

                for j in range(len(matriz_Salida)):
                    x = str(j + 1)
                    fila = matriz_Salida.index(j).value
                    for k in range(len(fila)):
                        y = str(k + 1)
                        dato = fila.index(k).value
                        nodo = ET.SubElement(doc, "dato", x=str(x), y=str(y))
                        nodo.text = str(dato)

                for j in range(len(frecuencia)):
                    nodo2 = ET.SubElement(doc, "frecuencia", g=str(frecuencia.index(j).value))
                    nodo2.text = str(g_frecuencia.index(j).value)

            arbol = ET.ElementTree(root)
            arbol.write(ruta_especifica)
        except:
            print('Ocurrio un error')
        continue

    if opcion == '4':
        time.sleep(0.1)
        print('''
> Diego Fernando Cortez Lopez
> 201900955
> Introduccion a la Programación y computación 2 seccion "A"
> Ingenieria en Ciencias y Sistemas
> 4to Semestre
        ''')
        continue

    if opcion == '5':
        time.sleep(0.1)
        print('\nGenerar gráfica')
        print('\nMatrices guardadas:\n')

        for i in range(len(matriz.nombre)):
            numeracion = str(i + 1) + "."
            print(numeracion, matriz.nombre.index(i))
            for j in range(len(matriz.dato.index(i).value)):
                print('\t', matriz.dato.index(i).value.index(j))
            print('')

        seleccion = input('Ingrese el nombre de una matriz: ')
        if matriz.nombre.buscar(seleccion):
            for i in range(len(matriz.nombre)):
                if seleccion == matriz.nombre.index(i).value:
                    nombre = matriz.nombre.index(i).value
                    n = matriz.fila.index(i).value
                    m = matriz.columna.index(i).value
                    matriz_Graficar = matriz.dato.index(i).value

                    dot = Digraph(nombre, "Reporte_Matriz")
                    dot.graph_attr["rankdir"] = "TD"

                    dot.node('Matrices', 'Matrices')
                    dot.node('nombre', nombre)
                    dot.node('n', 'n=' + str(n), _attributes={"shape": "doublecircle", "color": "blue"})
                    dot.node('m', 'm=' + str(m), _attributes={"shape": "doublecircle", "color": "blue"})
                    dot.edge('Matrices', 'nombre')
                    dot.edge('nombre', 'n')
                    dot.edge('nombre', 'm')

                    primeraFila = matriz_Graficar.index(0).value

                    for j in range(len(primeraFila)):
                        nuevaMatriz = ListaCircular()
                        for k in range(len(matriz_Graficar)):
                            filas = matriz_Graficar.index(k).value
                            nuevaMatriz.add(filas.index(j).value)
                        for k in range(len(nuevaMatriz)):
                            dato = nuevaMatriz.index(k).value
                            if k == 0:
                                dot.node('x=' + str(k) + 'y=' + str(j), str(dato))
                                dot.edge('nombre', 'x=' + str(k) + 'y=' + str(j))
                            else:
                                dot.node('x=' + str(k) + 'y=' + str(j), str(dato))
                                dot.edge('x=' + str(k-1) + 'y=' + str(j), 'x=' + str(k) + 'y=' + str(j))

                    dot.render("Reporte_Matriz", view=False, format="pdf")

        else:
            print('Nombre de la matriz no existe')

        continue

    if opcion == '6':
        break