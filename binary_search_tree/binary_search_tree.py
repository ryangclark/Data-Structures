class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    
    node = self
    while True:
      if new_node.value == node.value:
        return 'I don\'t know what to do with duplicates!'
      if new_node.value < node.value:
        if node.left:
          node = node.left
          continue
        else:
          node.left = new_node
          return
      if new_node.value > node.value:
        if node.right:
          node = node.right
          continue
        else:
          new_node.right = node.right
          node.right = new_node
          return    

  def contains(self, target):
    node = self
    while node != None:
      if target == node.value:
        return True
      if target < node.value:
        node = node.left
        continue
      if target > node.value:
        node = node.right
        continue

    return False

  def get_max(self):
    node = self
    while node.right != None:
      node = node.right
      continue

    return node.value

  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)

    if self.right:
      self.right.for_each(cb)
