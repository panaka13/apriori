import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.csv_database import CsvDatabase
from core.attr_value import AttributeValue
from core.itemset import ItemSet
from core.rule import Rule
from core.apriori import Apriori
from core.factory import Factory

from testcase import MyUnitTest 

class AprioriTest(MyUnitTest):
  path = os.path.join(os.getcwd(), 'test_data/contact-lenses.csv')

  def setUp(self):
    Factory.database = CsvDatabase(os.path.join(os.getcwd(), 'test_data/contact-lenses.csv'))

  def test_generate_rule(self):
    db = CsvDatabase(self.path)
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('spectacle-prescrip', 'myope')
    a3 = AttributeValue('astigmatism', 'yes')
    a4 = AttributeValue('tear-prod-rate', 'reduced')
    itemset = ItemSet.create_itemset(a1, a2, a3, a4)
    apriori = Apriori(db, 0, 0, 0)
    rules = apriori.generate_confident_rules(itemset)
    self.assertEqual(len(rules), 14)

  def test_generate_rule_confidence(self):
    db = CsvDatabase(self.path)
    a1 = AttributeValue('age', 'young')
    a2 = AttributeValue('spectacle-prescrip', 'myope')
    a3 = AttributeValue('astigmatism', 'yes')
    a4 = AttributeValue('tear-prod-rate', 'reduced')
    itemset = ItemSet.create_itemset(a1, a2, a3, a4)
    apriori = Apriori(db, 0, 0.5, 100)
    rules = apriori.generate_confident_rules(itemset)
    self.assertEqual(len(rules), 3)

  def test_generate_all_rule(self):
    db = CsvDatabase(self.path)
    apriori = Apriori(db, 0.3, 0.3, 10)
    confident_rules = apriori.generate_all_confidence_rules()
    self.assertEqual(len(confident_rules), 6)
    apriori = Apriori(db, 0.3, 0.3, 5)
    confident_rules = apriori.generate_all_confidence_rules()
    self.assertEqual(len(confident_rules), 5)


if __name__ == '__main__':
  unittest.main()
