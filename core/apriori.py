from core.database import Database
from core.itemset import ItemSet
from core.rule import Rule
from core.factory import Factory

class Apriori:
  """
  Class that implement Apriori algorithm.
  """
  def __init__(self, database: Database, 
      min_support, min_confidence, num_rules):
    self.database = database
    self.min_support = min_support
    self.min_confidence = min_confidence
    self.num_rules = num_rules

  def _extend_itemset_by_join(self, itemsets):
    candidate_itemsets = []
    for i in range(len(itemsets)):
      for j in range(i+1, len(itemsets)):
        if itemsets[i].distance(itemsets[j]) == 1:
          joined_itemset = itemsets[i].join(itemsets[j])
          # TODO: check pruning
          if joined_itemset not in candidate_itemsets:
            candidate_itemsets.append(joined_itemset)
    return candidate_itemsets

  def generate_frequent_itemset(self, global_itemset = None):
    frequent_itemsets = {}
    if global_itemset is None:
      global_itemset = self.database.get_distinct_attr_values()
    candidate_itemset = []
    for item in global_itemset:
      candidate_itemset.append(ItemSet.create_itemset(item))
    current_length = 1
    while True:
      # pruning
      frequent_itemset = [
          itemset for itemset in candidate_itemset 
          if itemset.support >= self.min_support]
      if len(frequent_itemset) == 0:
        break
      # print('L%d: %d frequennt itemset' % (current_length, len(frequent_itemset)))
      frequent_itemsets[current_length] = frequent_itemset
      current_length += 1
      # new candidate
      # TODO: make new candidate more efficient to check/insert
      candidate_itemset.clear()
      candidate_itemset = self._extend_itemset_by_join(frequent_itemset)
    return frequent_itemsets

  def _generate_rule(self, global_itemset: ItemSet, clause: ItemSet):
    result = global_itemset.new_remove(*clause.items)
    rule = Rule.create_fule(clause, result)
    return rule

  def generate_confident_rules(self, global_itemset = None):
    if global_itemset is None:
      global_attr = self.database.get_distinct_attr_values()
      global_itemset = ItemSet.create_itemset(*global_attr) 
    whole_support = global_itemset.support
    candidate_itemsets = []
    for item in global_itemset.items:
      candidate_itemsets.append(global_itemset.new_remove(item)) 
    confident_rules = []
    while True:
      confident_itemsets = [
          itemset for itemset in candidate_itemsets
          if (itemset.size() > 0) and 
          (whole_support / itemset.support  >= self.min_confidence)]
      confident_rules = confident_rules + confident_itemsets
      if len(confident_itemsets) == 0:
        break
      candidate_itemsets.clear()
      for itemset in confident_itemsets:
        if itemset.size() == 1:
          continue;
        for item in itemset.items:
          new_itemset = itemset.new_remove(item)
          if new_itemset not in candidate_itemsets:
            candidate_itemsets.append(new_itemset)
    return [self._generate_rule(global_itemset, rule) for rule in confident_rules]

  def generate_all_confidence_rules(self):
    frequent_itemsets = self.generate_frequent_itemset()
    confident_rules = []
    for level in frequent_itemsets:
      for itemset in frequent_itemsets[level]:
        confident_rules = confident_rules + self.generate_confident_rules(itemset) 
    if self.num_rules is not None:
      return sorted(confident_rules, reverse = True)[:self.num_rules]
    else:
      return sorted(confident_rules, reverse = True)
