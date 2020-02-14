from .attr_value import AttributeValue

class ItemSet:
  def __init__(self, *argv):
    self.items = []
    for item in argv:
      if isinstance(item, AttributeValue):
        if item not in self.items:
          self.items.append(item)

  def join(self, other):
    new_item_list = list(self.items)
    for item in other.items:
      if item not in new_item_list:
        new_item_list.append(item)
    return ItemSet(*new_item_list)

  def number_not_in(self, other):
    # TODO: make this faster
    counter = 0
    for item in self.items:
      if item not in other.items:
        counter += 1
    return counter

  def distance(self, other):
    # TODO: make this faster
    return max(self.number_not_in(other), other.number_not_in(self))

  def diff(self, other):
    # TODO: make this faster
    return self.number_not_in(other) + other.number_not_in(self)

  def isEmpty(self):
    return len(self.items) == 0
    
  def __str__(self):
    return 'itemset {{{0}}}'.format(','.join(map(str, self.items)))

  def __le__(self, other):
    if not isinstance(other, ItemSet):
      raise 'Cannot compare itemset with other structure'
    # TODO: make this faster
    for item in self.items:
      if item not in other.items:
        return False
    return True
