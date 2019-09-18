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
      # if it's self.left...
      if self.right:
        # insert the value to the left
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
    pass

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    pass

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass