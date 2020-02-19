import unittest
import os
import sys
sys.path.append(os.getcwd())

from core.csv_database import CsvDatabase
from core.factory import Factory

class MyUnitTest(unittest.TestCase):
  def setUp(self):
    db = CsvDatabase(os.path.join(os.getcwd(), 'test_data/contact-lenses.csv'))
    Factory.setup_db(db)
