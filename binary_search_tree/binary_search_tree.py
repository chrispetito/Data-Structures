import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None
    self.size = 0

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    # if value exists, return
    if value == self.value:
      return
    # if value is less than self.value...
    elif value < self.value:
      # if it's self.left...
      if self.left:
        # insert the value to the left
        self.left.insert(value)
      else:
        # else, recurse
        self.left = BinarySearchTree(value)
    else:
      # if it's self.right...
      if self.right:
        # insert the value to the right
        self.right.insert(value)
      else:
        # else, recurse
        self.right = BinarySearchTree(value)

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    # if self.value = target, return True
    if self.value == target:
      return True
    # if target is less than self.value...
    elif target < self.value:
      #if it is self.left...
      if self.left:
        # recurse
        return self.left.contains(target)
      # else, return False
      else:
        return False
    # if target is greater than or equal to self.value...
    elif target >= self.value:
      #if it is self.right...
      if self.right:
        # recurse
        return self.right.contains(target)
      # else, return False
      else:
        return False
      

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    current = self
    while current.right:
      current = current.right
    return current.value

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    if self.value == None:
      return
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

  # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):
      stack_name = Stack()
      ordered_list = []
      if node:
        stack_name.push(node)
        while stack_name.size > 0:
          variable = stack_name.pop()
          ordered_list.append(variable.value)
          if variable.right:
            stack_name.push(variable.right)
          if variable.left:
            stack_name.push(variable.left)
      new_list = sorted(ordered_list)
      for i in new_list:
        print(i)


  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  #   create a queue
  # put root in queue
  # while queue is not empty
  # pop first item in queue
  # check left and right add to queue
  # shift 
  # go to head of queue and continue'''
  def bft_print(self, node):
      cue_name = Queue()
      cue_name.enqueue(node)
      while cue_name.size > 0:
        variable = cue_name.dequeue()
        print(variable.value)
        if variable.left:
          cue_name.enqueue(variable.left)
        if variable.right:
          cue_name.enqueue(variable.right)


  def dft_print(self, node):
      # make a stack
      stack_name = Stack()
      # add node as root in stack
      stack_name.push(node)
      # while stack:
      while stack_name.size > 0:
        # pop first item in stack into variable
        variable = stack_name.pop()
        print(variable.value)
        # if var.right:
        if variable.left:
          # add to stack
          stack_name.push(variable.left)
        # elif var.left:
        if variable.right:
          # add to stack
          stack_name.push(variable.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass

