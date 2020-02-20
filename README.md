### requirement:
pandas >= 0.24.1

### tested os:
ubuntu 18.01

### to run:
`python3 main.py -i path/to/file.csv -m minimun\_support -n c minimum\_confidence -n numrule`

### for benchmark: 
`python3 benchmark.py` <br />
for benchmark, confidence is set to 0, and support is from 0.1 to 0.5 (where there are no rules with higher support).

### to test:
`python3 test/test\_script.py`

### structure:
- core: core package of the project, implementation of apriori algorithm and its supporting data structure
  - core.database: abstract class for our database. provide function to count support, confident, etc.  
  - core.csv_database: implementation to use with csv file
  - core.attr_value: fundamental item unit, defined over an column and its attribute. 
  - core.itemset: defined the itemset
  - core.rule: define the rule
  - core.apriori: implementation of apriori algorithm
- test: modules containing all unittests
- test_data: containing dataset used for testing and benchmark.
- main.py: main file for running
- benchmark.py: main file for running benchmark.

### issues:
- running time is very high (running benchmark for details) 
```
Support 0.10000, runtime 390.110582892, numrules 6090
Support 0.10404, runtime 370.372849130, numrules 5964
Support 0.10808, runtime 332.196668411, numrules 5700
...
```

### contributors:
[Khang Phan](https://github.com/panaka13) <br/>
[Jesus Salazar](https://github.com/Jesus588)
