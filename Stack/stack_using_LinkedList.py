"""
Author:Tayyrov
@CodeAcademy Practice
Implementation of Stack using Linked List

"""

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      return "Out of Space"

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The stack is Empty.")
  
  def peek(self):
    if self.size > 0:
	    return self.top_item.get_value()
    else:
      print("Stack is Empty!")
      
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0
