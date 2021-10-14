import math

class DoubleLinkedList:
  class Node:
    #Metodo inicializador de la clase Nodo
    def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None
  #Metodo inicializador de la clase Double_Linked_List
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def show_elements(self):
    array = []
    current_node = self.head
    while current_node != None:
      array.append(current_node.value)
      current_node = current_node.next
    return print(array)  

  def show_menu(self):
    option_menu = 0
    while option_menu != 3:
      try:
        option_menu = int(input('\nSeleccione una opción:' + '\n 1. ' +  'Eliminar nodo' + '\n 2. ' + 'Invertir la lista' + '\n 3. ' + 'Invertir la lista elevando valores al cuadrado' +  '\n 4. ' + 'Salir\n Su respuesta: '))

        if option_menu == 1:
          self.remove()

        elif option_menu == 2:
          self.reverse()

        elif option_menu == 3:
          self.reversePow()
        
        elif option_menu == 4:
          break
           
        else:
          print('\n Opción no valida ')

      except ValueError:
        print('\n Ingrese un número ')

  def initialize_append(self):
    while True:
      try:
        cant_node = int(input('\n     Cantidad de nodos a crear: '))
        for node_item in range(cant_node):
          value = int(input('\n     Ingrese el valor del nodo: '))
          new_node = self.Node(value)
          if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
          else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
          self.length += 1
        print('\n')
        self.show_elements()
        break
      except ValueError:
        print('\nSe espera un numero ')        
  def remove(self):
    while True:
      try:
        index = int(input('\n     Ingrese el indice: '))
        while True:
          if index < 0 or index+1 > self.length:
            print('\n Indice por fuera de los limites')
            index = int(input('\n     Ingrese el indice: '))
          else:
            break
        break
      except ValueError:
        print('\n Se espera un numero')
    if index == 0:
      self.shift()
      print('\n Eliminado con exito')
      self.show_elements()
    elif index == self.length-1:
      self.pop()
      print('\n Eliminado ')
      self.show_elements()
    else:
      prev_node = self.get(index-1)
      next_node = self.get(index+1)
      prev_node.next = next_node
      next_node.prev = prev_node
      self.length -= 1
      print('\n Eliminado')
      self.show_elements()
  
  #Metodo para invertir la lista
  def reverse(self):
    prev_node = None
    current_node = self.head
    self.head.prev = None
    while current_node != None:
      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node
      current_node = current_node.prev
    self.head = prev_node.prev
    print('\nLista invertida')
    self.show_elements()

#Invertir y elevar al cuadrado
  def reversePow(self):
    prev_node = None
    current_node = self.head
    self.head.prev = None
    while current_node != None:
      prev_node = current_node.prev
      current_node.prev = current_node.next
      current_node.next = prev_node
      current_node.value = current_node.value ** 2
      current_node = current_node.prev
    self.head = prev_node.prev
    print('\n Lista invertida y elevada al cuadrado')
    self.show_elements()

  #Eliminar el ultimo elemento de la lista
  def pop(self):
    if self.length == 0 or self.length == 1:
      self.head = None
      self.tail = None
    else:
      current_node = self.tail
      temp = current_node.prev
      temp.next = None
      temp = None
      self.tail = current_node.prev  

#Obtener el valor de un nodo a partir del indice
  def get(self, index):
    if index == 0:
      return self.head
    elif index == self.length-1:
      return self.tail
    elif not(index >= self.length or index < 0):
      current_node = self.head
      visit_node_count = 0
      while visit_node_count != index:
        current_node = current_node.next
        visit_node_count += 1
      return current_node
    else:
      return None

 #Eliminar primer elemento de la lista
  def shift(self):
    if self.length == 0:
      self.head = None
      self.tail = None
    else:
      delete_node = self.head
      self.head = delete_node.next
      delete_node.next = None
      delete_node.prev = None
      self.length -= 1
       