class Node:
    def __init__(self, data):
        self.valor = data
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.total = 0

    def is_empty(self):
        return self.inicio == None

    def size(self):
        return self.total

    def insert_beginning(self, value):
        novo = Node(value)
        novo.proximo = self.inicio
        self.inicio = novo
        self.total += 1

    def insert_end(self, value):
        novo = Node(value)
        if self.is_empty():
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo != None:
                atual = atual.proximo
            atual.proximo = novo
        self.total += 1

    def search(self, value):
        atual = self.inicio
        while atual != None:
            if atual.valor == value:
                return True
            atual = atual.proximo
        return False

    def remove(self, value):
        if self.is_empty():
            return False

        if self.inicio.valor == value:
            self.inicio = self.inicio.proximo
            self.total -= 1
            return True

        anterior = self.inicio
        atual = self.inicio.proximo
        
        while atual != None:
            if atual.valor == value:
                anterior.proximo = atual.proximo
                self.total -= 1
                return True
            anterior = atual
            atual = atual.proximo
            
        return False

    def print_list(self):
        atual = self.inicio
        while atual != None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

# teste
if __name__ == "__main__":
    lista = LinkedList()
    lista.insert_beginning(10)
    lista.insert_end(20)
    lista.insert_beginning(5)
    lista.print_list()
    lista.remove(10)
    lista.print_list()
    print("Tamanho:", lista.size())