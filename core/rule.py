from functools import total_ordering

from core.itemset import ItemSet
from core.factory import Factory

@total_ordering
class Rule(Factory):
  def __init__(self, clause: ItemSet, result: ItemSet):
    self.clause = clause
    self.result = result
    self.confidence = -1

  @classmethod
  def create_fule(cls, clause: ItemSet, result: ItemSet):
    whole = clause.join(result)
    rule = Rule(clause, result)
    rule.confidence = whole.support / clause.support
    return rule

  def __str__(self):
    return '{0} => {1}'.format(self.clause, self.result)

  def __lt__(self, other):
    if not isinstance(self, ItemSet):
      raise 'Cannot compare rule with other structure'
    if self.confidence != other.confidence:
      return self.confidence < other.confidence
    return self.clause.support < other.clause.support
