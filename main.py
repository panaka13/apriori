import argparse
from core.apriori import Apriori
from core.csv_database import CsvDatabase
from core.factory import Factory

class Setting:
  pass

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', '-i',
      help = 'input file (csv file)')
  parser.add_argument('--minsup', '-m', type=float, help='minimum support')
  parser.add_argument('--minconf', '-c', type=float, help='minimun confidence')
  parser.add_argument('--numrule', '-n', type=int, 
      help='max number of rules output')
  args = parser.parse_args()

  db = CsvDatabase(args.input)
  Factory.setup_db(db)
  apriori = Apriori(db, args.minsup, args.minconf, args.numrule)
  frequent_itemsets = apriori.generate_frequent_itemset()
  for level in frequent_itemsets:
    print(level, ': ', len(frequent_itemsets[level]))
    for itemset in frequent_itemsets[level]:
      print(itemset)
  print('Rules:')
  for rule in apriori.generate_all_confidence_rules():
    print(rule, '(confidence: %.4f)' % (rule.confidence))

if __name__ == "__main__":
  main() 
