from .database import Database
from .itemset import ItemSet

class Apriori:
  """
  Class that implement Apriori algorithm.
  """
  def __init__(self, database: Database, min_support):
    self.database = database
    self.min_support = min_support

  def run(self, global_itemset = None):
    frequent_itemsets = {}
    if global_itemset is None:
      global_itemset = self.database.get_distinct_attr_values()
    candidate_itemset = []
    for item in global_itemset:
      candidate_itemset.append(ItemSet(item))
    current_length = 1
    while True:
      # pruning
      frequent_itemset = [
          itemset for itemset in candidate_itemset 
          if self.database.support(itemset) >= self.min_support]
      print('len ', len(frequent_itemsets)+1, ': ', len(frequent_itemset))
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
            if joined_itemset not in candidate_itemset:
              candidate_itemset.append(joined_itemset)
    return frequent_itemsets

  def generate_rules(self, global_itemset = None):
    if global_itemset is None:
      global_itemset = self.database.get_distinct_attr_values()
