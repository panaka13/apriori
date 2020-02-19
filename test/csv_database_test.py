import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.csv_database import CsvDatabase
from core.attr_value import AttributeValue
from core.itemset import ItemSet

from testcase import MyUnitTest

class CsvDatabaseTest(MyUnitTest):
  path = os.path.join(os.getcwd(), 'test_data/contact-lenses.csv')

  def _check(self, attr, value, attr_values):
    self.assertTrue(AttributeValue(attr, value) in attr_values)
  
  def test_support_count(self):
    db = CsvDatabase(self.path)
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('spectacle-prescrip', 'myope')
    set1 = ItemSet.create_itemset(a1)
    self.assertEqual(db.support_count(set1), 8)
    set2 = ItemSet.create_itemset(a1, a2)
    self.assertEqual(db.support_count(set2), 4)
    self.assertEqual(db.counter, 5)

  def test_distinct_attr_value(self):
    db = CsvDatabase(self.path)
    attr_values = db.get_distinct_attr_values()
    self.assertEqual(len(attr_values), 12)
    self._check('age', 'young', attr_values)
    self._check('age', 'pre-presbyopic', attr_values)
    self._check('age', 'presbyopic', attr_values)
    self._check('spectacle-prescrip', 'myope', attr_values)
    self._check('spectacle-prescrip', 'hypermetrope', attr_values)

  def test_confidence(self):
    db = CsvDatabase(self.path)
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('spectacle-prescrip', 'myope')
    a3 = AttributeValue('astigmatism', 'yes')
    set1 = ItemSet.create_itemset(a1, a2)
    set2 = ItemSet.create_itemset(a3)
    self.assertEqual(db.confidence(set1, set2), 2/4)

if __name__ == '__main__':
  unittest.main()
