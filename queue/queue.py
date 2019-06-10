class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.size += 1
    return self.storage.append(item)
  
  def dequeue(self):
    if not self.size:
      return None

    self.size -= 1
    return self.storage.pop(0)

  def len(self):
    return self.size
