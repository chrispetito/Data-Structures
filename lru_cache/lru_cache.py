# import sys
# sys.path.append('../doubly_linked_list.py')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.nodes = 0
    self.cache = {}
    self.storage = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # if key isn't in cache return None
    if key not in self.cache:
      return None
    # else, set node to the key in cache, delete node from storage, add key and node to storage head and return node value
    else:
      node = self.cache[key]
      self.storage.delete(node[1])
      self.storage.add_to_head([key, node[0]])
      return node[0]


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # if key exists in cache...
    if key in self.cache:
      # set var to node
      node = self.cache[key]
      # delete node from storage
      self.storage.delete(node[1])
      # add node to storage head
      self.storage.add_to_head([key, value])
      # set cache node to storage node
      self.cache[key] = [value, self.storage.head]
      return
    # if cache is at max capacity...  
    elif self.limit is self.nodes:
      # remove tail node from storage and cache
      node_value = self.storage.tail
      self.storage.remove_from_tail()
      del self.cache[node_value.value[0]]
      self.nodes -= 1
    # add new node to head
    self.storage.add_to_head([ key, value ])
    self.cache[key] = [value, self.storage.head]
    self.nodes += 1
