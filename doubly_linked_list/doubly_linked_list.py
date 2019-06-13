"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if not self.head and not self.tail:
      new_node = ListNode(value, self.head, self.tail)
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

    self.length += 1

  def remove_from_head(self):
    if not self.head and not self.tail:
      return None

    if self.head is self.tail:
      self.tail = None

    old_head = self.head
    self.head = old_head.next
    self.length -= 1

    return old_head.value

  def add_to_tail(self, value):
    if not self.head and not self.tail:
      new_node = ListNode(value, self.head, self.tail)
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

    self.length += 1
    
  def remove_from_tail(self):
    if not self.head and not self.tail:
      return None

    if self.head is self.tail:
      self.head = None

    old_tail = self.tail
    self.tail = old_tail.prev
    self.length -= 1

    return old_tail.value

  def move_to_front(self, node):
    if node is self.head:
      return None

    self.delete(node)

    return self.add_to_head(node.value)

  def move_to_end(self, node):
    if node is self.tail:
      return None

    self.delete(node)
    
    return self.add_to_tail(node.value)

  def delete(self, node):
    if not self.head and not self.tail:
      return None
    elif node is self.head:
      return self.remove_from_head()
    elif node is self.tail:
      return self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    
  def get_max(self):
    if not self.head and not self.tail:
      return None

    current = self.head
    res = current.value

    while current:
      if current.value > res:
        res = current.value
      current = current.next

    return res 
