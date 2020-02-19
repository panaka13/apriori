import numpy  as np
import time
import matplotlib.pyplot as plt

from core.csv_database import CsvDatabase
from core.factory import Factory
from core.apriori import Apriori

interval = 100
low_support = 0.1
high_support = 0.5
confidence = 0

def graph_runtime(runtimes):
  plt.plot(np.linspace(low_support, high_support, interval), runtimes, label = 'runtime over support')
  plt.xlabel('support')
  plt.ylabel('runtime (in second)')
  plt.legend()
  plt.savefig('runtime.png')
  plt.close()

def graph_numrules(numrules):
  plt.plot(np.linspace(low_support, high_support, interval), numrules, label = 'runtime over support')
  plt.xlabel('support')
  plt.ylabel('number of rules')
  plt.legend()
  plt.savefig('numrules.png')
  plt.close()

def main():
  db = CsvDatabase('test_data/zero_one.csv')
  Factory.setup_db(db)
  runtimes = [] # store runtime (in second)
  numrules = [] # store number of confident rules
  for support in np.linspace(low_support, high_support, interval):
    start_time = time.monotonic()
    apriori = Apriori(db, support, confidence, None)
    rules = apriori.generate_all_confidence_rules()
    #for rule in rules:
    #  print(rule, ': ', rule.confidence)
    end_time = time.monotonic()
    runtimes.append(end_time - start_time)
    numrule = len(rules)
    numrules.append(numrule)
    print('Support %.2f, runtime %.9f, numrules %d' % (support, end_time - start_time, numrule))
  graph_runtime(runtimes)
  graph_numrules(numrules)

if __name__ == '__main__':
  main()
