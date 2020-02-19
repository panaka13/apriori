import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.attr_value import AttributeValue
from core.itemset import ItemSet

from testcase import MyUnitTest

class ItemSetTest(MyUnitTest):
  def test_diff(self):
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('age', 'pre-presbyopic')
    a3 = AttributeValue('age', 'presbyopic')
    a4 = AttributeValue('contact-lenses', 'none')
    set1 = ItemSet.create_itemset(a1, a2, a3)
    set2 = ItemSet.create_itemset(a2, a3, a4)
    set3 = ItemSet.create_itemset(a1, a4)
    set4 = ItemSet.create_itemset()
    self.assertEqual(set1.diff(set2), 2,
        '{0} and {1} does not have correct diff'.format(set1, set2))
    self.assertEqual(set2.diff(set3), 3,
        '{0} and {1} does not have correct diff'.format(set2, set3))
    self.assertEqual(set3.diff(set4), 2,
        '{0} and n{1} does not have correct diff'.format(set3, set4))
    self.assertEqual(set4.diff(set1), 3,
        '{0} and {1} does not have correct diff'.format(set4, set1))


  def test_join(self):
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('age', 'pre-presbyopic')
    a3 = AttributeValue('age', 'presbyopic')
    a4 = AttributeValue('contact-lenses', 'none')
    set1 = ItemSet.create_itemset(a1, a2, a3)
    set2 = ItemSet.create_itemset(a1, a4)
    set3 = set2.join(set1)
    self.assertEqual(len(set3.items), 4)
    self.assertTrue(a1 in set3.items)
    self.assertTrue(a2 in set3.items)
    self.assertTrue(a3 in set3.items)
    self.assertTrue(a4 in set3.items)

  def test_equality(self):
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('age', 'pre-presbyopic')
    set1 = ItemSet.create_itemset(a1, a2)
    set2 = ItemSet.create_itemset(a2, a1)
    self.assertEqual(set1, set2)


if __name__ == '__main__':
  unittest.main()
