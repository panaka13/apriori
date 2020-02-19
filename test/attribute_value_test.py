import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.attr_value import AttributeValue
from testcase import MyUnitTest

class AttributeValueTest(MyUnitTest):
  def test_equality(self):
    a1 = AttributeValue('a', 1)
    a2 = AttributeValue('a', 1)
    self.assertEqual(a1, a2)

if __name__ == '__main__':
  unittest.main()

