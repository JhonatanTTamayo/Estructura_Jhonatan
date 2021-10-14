class DoublelinkedLinkd:
  #Listas doblemente enlazadas
  class Nodo:
    def __init__(self,value):
      self.value = value
      self.previous_node = None
      self.next_node = None
  #Constructor de la clase nodo    

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def show_elements_list(self):
    array=[] 
    current_node = self.head
    #Mientras si exista un nodo entonces
    while current_node!=None:
      array.append(current_node.value)
      current_node = current_node.next_node
    return print(array)

  def append(self,value):
    new_node = self.Nodo(value)  
    if self.head == None and self.tail == None:
      self.head= new_node
      self.tail = self.head
    else:
      self.tail.next_node = new_node
      new_node.previous_node  = self.tail
      self.tail = new_node
    self.length +=1
    return print(new_node.value)  

  def unshift(self,value):
    new_node = self.Nodo(value)  
    if self.head == None and self.tail == None:
      self.head= new_node
      self.tail = self.head
    else:
      self.head.previous_node = new_node
      new_node.next_node=self.head
      self.head= new_node
    self.length +=1
    return print(new_node.value)

  def pop(self):
    if self.length ==1:
      self.head= None
      self.tail = None
    else:
      remove_node = self.tail
      self.tail = remove_node.previous_node
      self.tail.next_node = None
      remove_node.previous_node = None
    self.length -=1
    return print(remove_node.value)

  def shift(self): 
    if self.length ==1:
      self.head= None
      self.tail = None
    elif self.head !=None:
      remove_node = self.head
      self.head = remove_node.next_node
      remove_node.previous_node = None
      self.head = remove_node.next_node
      self.length -=1
    else:
      return None
    return print(remove_node.value)  

  def get(self, index):
    cont_posicion =1
    if index == self.length:
      print(self.tail.value)
      return self.tail
    elif index ==1:
      print(self.head.value)
      return print(self.head.value)  
    elif not (index < 1 or index >self.length):
      current_node = self.head
      while cont_posicion !=index:
        current_node= current_node.next_node
        cont_posicion +=1
        print(current_node.value)
        return current_node
      else:
        return None    

  def set(self, index, value):
    update_node = self.get(index)
    if update_node !=None:
      update_node.value= value
    else:
      return None 

  def insert(self, index, value):
    if index == self.lenght:
      return self.append(value)
    elif not (index <1 or index >self.lenght):
      new_node = self.Nodo(value)
      preview_node = self.get(index)
      next_node = preview_node.next_node
      preview_node.next_node = new_node
      new_node.previous_node = preview_node
      new_node.previous_node = new_node
      next_node.next_node = next_node
      self.lenght += 1
    else:
      return None

  def reverse(self):
    
    int_list=[5,15,30,50,70]
    int_list.reverse()
    print(int_list)

  def eliminarEnLista(una_lista):
    posicion = input("¿En que indice desea eliminar de la lista: " + ",".join(una_lista) + " ? ")
    if(str(posicion).isdigit() and int(posicion) <= len(una_lista)):
        una_lista.pop(int(posicion))
        return ",".join(una_lista)
    else:
        return "Algo anda mal"

  print(eliminarEnLista(["a", "b", "c", "d", "e"]))