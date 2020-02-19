from core.attr_value import AttributeValue
from core.factory import Factory

class ItemSet(Factory):
  def __init__(self, items):
    self.items = []
    self.support = -1
    for item in items:
      if isinstance(item, AttributeValue):
        if item not in self.items:
          self.items.append(item)

  def join(self, other):
    new_item_list = list(self.items)
    for item in other.items:
      if item not in new_item_list:
        new_item_list.append(item)
    return ItemSet.create_itemset(*new_item_list)

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

  def new_remove(self, *args):
    new_set = []
    for item in self.items:
      if item not in args:
        new_set.append(item)
    return ItemSet.create_itemset(*new_set)

  def new_add(self, *args):
    new_set = []
    for item in self.items:
      new_set.append(item)
    for item in args:
      if item not in new_set:
        new_set.append(item)
    return ItemSet.create_itemset(*new_set)
  
  def size(self):
    return len(self.items)
    
  def __str__(self):
    return 'itemset {{{0}}}'.format(','.join(map(str, self.items)))

  def __eq__(self, other):
    if not isinstance(other, ItemSet):
      raise 'Cannot compare itemset with other structure'
    return self.diff(other) == 0

  @classmethod
  def create_itemset(cls, *args):
    items = []
    for item in args:
      if item not in items:
        items.append(item)
    itemset = ItemSet(items)
    itemset.support = cls.database.support(itemset)
    return itemset
