class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)

    up = len(self.storage) - 1

    while up:
      up = self._bubble_up(up)

  def delete(self):
    length = len(self.storage)
    print('delete', self.storage)
    if length == 0:
      return None
    elif length == 1:
      return self.storage.pop()
    

    deleted = self.storage[0]
    self.storage[0] = self.storage.pop()
    down = 0

    while True:
      print('while loop down:', down)
      down = self._sift_down(down)
      if down:
        continue
      else:
        return deleted

  def get_max(self):
    return self.storage[0] if self.storage else None

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    '''Moves the element at the specified index "up" the heap
    by swapping it with its parent if the parent's value is less than the
    value at the specified index.'''

    parent_index = (index - 1) // 2

    if self.storage[parent_index] < self.storage[index]:
      self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
      return parent_index
    return False

  def _sift_down(self, index):
    '''Grabs the indices of this element's children and
    determines which child has a larger value. If the larger child's
    value is larger than the parent's value, the child element is swapped
    with the parent.'''
    
    left = None
    right = None
    
    if len(self.storage) > 2 * index + 1:
      left = 2 * index + 1

    if len(self.storage) > 2 * index + 2:
      right = 2 * index + 2

    larger = None
    
    if left:
      if right:
        if self.storage[left] >= self.storage[right]:
          larger = left
        else:
          larger = right
      else:
        larger = left

      if larger and self.storage[larger] > self.storage[index]:
        self.storage[index], self.storage[larger] = self.storage[larger], self.storage[index]
        return larger
      else:
        return False
    return False
        
    
