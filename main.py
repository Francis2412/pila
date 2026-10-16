from stack import Stack
from stack import Node
from stack import Producto

def main():
    pila = Stack()
    prod = Producto("P-01", "Mascarilla", 15.23, 6200)
    nodo = Node(prod)
    pila.push(nodo)
    prod = Producto("P-02", "Alcohol", 64.54, 1000)
    nodo = Node(prod)
    pila.push(nodo)
    prod = Producto("P-03", "vitamina", 21.85, 7000)
    nodo = Node(prod)
    pila.push(nodo) 
    

