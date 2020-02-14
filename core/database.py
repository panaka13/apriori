class Database: 
  def __init__(self, path):
    self.path = path
    self.counter = 0

  def get_distinct_attr_values(self):
    pass

  def support_count(self, itemset):
    pass

  def support(self, itemset):
    pass

  def confidence(self, clause, result, sup_clause = None, sup_whole = None):
    pass

  def increase_counter(self):
    self.counter += 1
