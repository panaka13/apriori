import pandas

from core.database import Database
from core.itemset import ItemSet
from core.attr_value import AttributeValue

class CsvDatabase(Database):
  def __init__(self, path):
    super().__init__(path)
    self.df = pandas.read_csv(path)
    self.num_entries = len(self.df)

  def get_distinct_attr_values(self):
    super().increase_counter()
    attr_values = []
    for attr in self.df.columns:
      for value in self.df[attr].unique():
        attr_values.append(AttributeValue(attr, value))
    return attr_values

  def support_count(self, itemset: ItemSet):
    super().increase_counter()
    if itemset.isEmpty():
      return len(self.df)
    df = self.df
    for item in itemset.items:
      super().increase_counter()
      df = df[df[item.attr] == item.value]
    return len(df)

  def support(self, itemset: ItemSet):
    return self.support_count(itemset) / self.num_entries

  def confidence(self, clause, result, sup_clause = None, sup_whole = None):
    if sup_clause is None:
      sup_clause = self.support_count(clause)
    if sup_whole is None:
      whole = clause.join(result)
      sup_whole = self.support_count(whole)
    return sup_whole / sup_clause
