import argparse
from core.apriori import Apriori
from core.csv_database import CsvDatabase

class Setting:
  pass

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', '-i',
      help = 'input file (csv file)')
  parser.add_argument('--minsup', '-m', type=float, help='minimum support')
  args = parser.parse_args()

  apriori = Apriori(CsvDatabase(args.input), args.minsup)
  frequent_itemsets = apriori.run()
  for level in frequent_itemsets:
    print(level)
    for itemset in frequent_itemsets[level]:
      print(itemset)

if __name__ == "__main__":
  main() 
