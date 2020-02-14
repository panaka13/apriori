class AttributeValue: 
  def __init__(self, attr, value):
    self.attr = attr;
    self.value = value;
  
  def __str__(self):
    return '({0}: {1})'.format(self.attr, self.value)

  def __eq__(self, other):
    if not isinstance(other, AttributeValue):
      raise 'Cannot compare AttributeValue with another type'
    return self.attr == other.attr and self.value == other.value
