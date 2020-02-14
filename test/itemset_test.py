import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.attr_value import AttributeValue
from core.itemset import ItemSet


class ItemSetTest(unittest.TestCase):
  def test_diff(self):
    a1 = AttributeValue('a', 1)
    a2 = AttributeValue('a', 2)
    a3 = AttributeValue('a', 3)
    a4 = AttributeValue('a', 4)
    set1 = ItemSet(a1, a2, a3)
    set2 = ItemSet(a2, a3, a4)
    set3 = ItemSet(a1, a4)
    set4 = ItemSet()
    self.assertEqual(set1.diff(set2), 2,
        '{0} and {1} does not have correct diff'.format(set1, set2))
    self.assertEqual(set2.diff(set3), 3,
        '{0} and {1} does not have correct diff'.format(set2, set3))
    self.assertEqual(set3.diff(set4), 2,
        '{0} and n{1} does not have correct diff'.format(set3, set4))
    self.assertEqual(set4.diff(set1), 3,
        '{0} and {1} does not have correct diff'.format(set4, set1))


  def test_join(self):
    a1 = AttributeValue('a', 1)
    a2 = AttributeValue('a', 2)
    a3 = AttributeValue('a', 3)
    a4 = AttributeValue('a', 4)
    set1 = ItemSet(a1, a2, a3)
    set2 = ItemSet(a1, a4)
    set3 = set2.join(set1)
    self.assertEqual(len(set3.items), 4)
    self.assertTrue(a1 in set3.items)
    self.assertTrue(a2 in set3.items)
    self.assertTrue(a3 in set3.items)
    self.assertTrue(a4 in set3.items)


if __name__ == '__main__':
  unittest.main()
