#Definición de la estructura de datos
class Producto:
    def __init__(self,cod:str, nombre:str, precio:float,stock:int):
        self.cod =cod
        self.nombre =nombre
        self.precio = precio
        self.stock = stock
        self.next = None
 

class Stack:
    def __init__(self):
        self.top=None

        #operaciones de la pila
    def isEmpty(self)->bool:
        if self.top == None:
             return True
        else:
            return False

    def push(self,new:Producto):
        if self.isEmpty():
            self.top=new
        else: 
            new.next = self.top 
            self.top=new

