class Node(object):

    def __init__(self, value):
         self.value = value
         self.next = None

    def __str__(self):
        return str(self.value)

    def get(self):
        return self.value


class ListaCircular(object):

    def __init__(self):
        self.first = None
        self.size = 0

    def add(self, dato):
        NewNodo = Node(dato)
        if self.size == 0:
            self.first = NewNodo
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = NewNodo
        self.size += 1
        return NewNodo

    def index(self, numero):
        current = self.first
        for i in range(len(self)):
            if i == numero:
                return current
            current = current.next

    def buscar(self, dato):
        current = self.first
        encontrado = False
        try:
            for i in range(len(self)):
                while encontrado != True:
                    if dato == current.value:
                        encontrado = True
                    current = current.next
        except:
            encontrado = False
        return encontrado

    def __len__(self):
        return self.size

    def recorrer(self):
        current = self.first
        for i in range(len(self)):
            print('current = ', current)
            current = current.next

    def __str__(self):
        String = "["
        current = self.first
        for i in range(len(self)):
            String += str(current)
            if i != len(self) - 1:
                String += str(", ")
            current = current.next
        String += "]"
        return String