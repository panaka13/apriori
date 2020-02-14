import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.csv_database import CsvDatabase
from core.attr_value import AttributeValue
from core.itemset import ItemSet

class CsvDatabaseTest(unittest.TestCase):
  path = os.path.join(os.getcwd(), 'test_data/contact-lenses.csv')

  def _check(self, attr, value, attr_values):
    self.assertTrue(AttributeValue(attr, value) in attr_values)
  
  def test_support_count(self):
    db = CsvDatabase(self.path)
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('spectacle-prescrip', 'myope')
    set1 = ItemSet(a1)
    self.assertEqual(db.support_count(set1), 8)
    set2 = ItemSet(a1, a2)
    self.assertEqual(db.support_count(set2), 4)
    self.assertEqual(db.counter, 3)

  def test_distinct_attr_value(self):
    db = CsvDatabase(self.path)
    attr_values = db.get_distinct_attr_values()
    self.assertEqual(len(attr_values), 12)
    self._check('age', 'young', attr_values)
    self._check('age', 'pre-presbyopic', attr_values)
    self._check('age', 'presbyopic', attr_values)
    self._check('spectacle-prescrip', 'myope', attr_values)
    self._check('spectacle-prescrip', 'hypermetrope', attr_values)


if __name__ == '__main__':
  unittest.main()
