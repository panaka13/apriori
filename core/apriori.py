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

  def generate_frequent_itemset(self, global_itemset = None):
    frequent_itemsets = {}
    if global_itemset is None:
      global_itemset = self.database.get_distinct_attr_values()
    candidate_itemset = []
    for item in global_itemset:
      candidate_itemset.append(Factory.create_itemset(item))
    current_length = 1
    while True:
      # pruning
      frequent_itemset = [
          itemset for itemset in candidate_itemset 
          if itemset.support >= self.min_support]
      if len(frequent_itemset) == 0:
        break
      frequent_itemsets[current_length] = frequent_itemset
      current_length += 1
      # new candidate
      # TODO: make new candidate more efficient to check/insert
      candidate_itemset.clear()
      for i in range(len(frequent_itemset)):
        for j in range(i+1, len(frequent_itemset)):
          if frequent_itemset[i].distance(frequent_itemset[j]) == 1:
            joined_itemset = frequent_itemset[i].join(frequent_itemset[j])
            # TODO: check pruning
            if joined_itemset not in candidate_itemset:
              candidate_itemset.append(joined_itemset)
    return frequent_itemsets

  def _generate_rule(self, global_itemset: ItemSet, clause: ItemSet):
    result = global_itemset.new_remove(*clause.items)
    rule = Rule.create_fule(clause, result)
    return rule

  def generate_confident_rules(self, global_itemset = None):
    if global_itemset is None:
      global_itemset = self.database.get_distinct_attr_values()
    whole_support = global_itemset.support
    candidate_itemsets = []
    for item in global_itemset.items:
      candidate_itemsets.append(global_itemset.new_remove(item)) 
    confident_rules = []
    while True:
      confident_itemsets = [
          itemset for itemset in candidate_itemsets
          if whole_support / itemset.support  >= self.min_confidence]
      confident_rules = confident_rules + confident_itemsets
      candidate_itemsets.clear()
      for itemset in confident_itemsets:
        if itemset.size() == 1:
          continue;
        for item in itemset.items:
          new_itemset = itemset.new_remove(item)
          if new_itemset not in candidate_itemsets:
            candidate_itemsets.append(new_itemset)
      if len(candidate_itemsets) == 0:
        break
    return [self._generate_rule(global_itemset, rule) for rule in confident_rules]

  def generate_all_confidence_rules(self):
    frequent_itemset = self.generate_frequent_itemset()
    confident_rules = []
    for itemset in frequent_itemsets:
      confident_rules = confident_rules + self.generate_confident_rules(itemset) 
    return sorted(confident_rules, reverse = True)[:self.num_rules]
