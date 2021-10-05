import math
from colorama import Fore, init
init()

class Activity_SLL:
  class Node:
    #Creamojs el método inicializador de la clasr nodo
    def __init__(self,value):
      self.value = value
      self.next = None
  #Creamos el méotod inicializador de la clase Single_Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
   
    
  def append(self):
    while True:
      try:
        cant_node = int(input(Fore.CYAN+'       Cantidad de nodos a que deseas crear: '+Fore.RESET))
        for node_item in range(cant_node):
          value = input(Fore.CYAN+'         Ingresa el valor del nodo: '+Fore.RESET)
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
          else:
            self.tail.next = new_node
            self.tail = new_node
          self.length +=1
        self.show_elements()
        menu_option = int(input(Fore.YELLOW+'    Seleccionar una opción del menu\n'+Fore.RESET+    Fore.RED+'      1. Añadir nodo con raiz cuadrada\n'    '      2. Eliminar y Añadir al final elevado al cuadrado\n'    '      3.Invertir la lista'+Fore.RESET))
        while True:
          if menu_option !=1 and menu_option!=2:
            menu_option = int(input('    Seleccionar una opcion del munu    1. Añadir nodo con raiz cuadrada    2. Eliminar y Añadir al final elevado al cuadrado    3.Invertir la lista'))
          elif menu_option==1:
            self.punto1()
            self.show_elements()
            break 
          elif menu_option ==2:
            self.punto2()
            self.show_elements()   
            break
          else:
            self.punto2()  
            break
        break
      except ValueError:
        print(Fore.RED+'           ERROR, se esperaba un valor númerico'+Fore.RESET)    

  def shift(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      self.length -= 1
      return print(delete_node.value)

  def punto1(self):
    index = int(input(Fore.CYAN+'       Ingresa el indice: '+Fore.RESET))
    new_node = self.get(index - 1)
    node_sqrt = math.sqrt(int(new_node.value))
    node_n =self.Node(node_sqrt)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
    else:
      node_n.next = self.head
      self.head = node_n
    self.length += 1

    
  def punto2(self):
    index = int(input(Fore.CYAN+'     Ingrese el indice: '+Fore.RESET))
    if index ==0:
      return self.shift()
    elif index == self.length-1 :
      return self.pop() 
    elif not index>=self.length or index < 0:
      preview_node=self.get(index-1)
      delete_node=preview_node.next
      preview_node.next = delete_node.next
      delete_node.next =None
      self.new_node_pow(index)
      self.length-=1
    else:
      return None  
  
  def new_node_pow(self, delete_node):
    index = int(input(Fore.CYAN+'       Ingresa el indice: '+Fore.RESET))
    new_node = self.get(index - 1)
    node_pow = math.pow(int(new_node.value),2)
    node_n =self.Node(node_pow)
    if self.head == None and self.tail == None:
      self.head = node_n
      self.tail = node_n
    else:
      self.tail.next = node_n
      self.tail = node_n
    self.length +=1

  def punto3(self):
    reverse_nodes = None
    current_node = self.head
    self.tail = current_node

    while current_node !=None:
      next = current_node.next
      current_node.next = reverse_nodes
      reverse_nodes=current_node
      current_node=next
    self.head = reverse_nodes  
    print(self.head)
  
  def show_elements(self):
    array= []
    current_node = self.head
    while current_node != None:
      #Mientras si exista un elemento en la cabeza de la lista, el valor se añade a la lista array
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)

  def get(self, index):
    if index == self.length -1:
      return self.tail
    if index == 0:
      return self.head
    elif not(index >= self.length or index <0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      return current_node
    else:
      return None

  