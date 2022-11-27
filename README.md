# Floyd-Warshall Algorithm with Imperative and Recursive Solutions

## Description
All pairs shortest path problems can be solved using the __Floyd-Warshall Algorithm__. The challenge here is to determine which pairs of nodes within a particular edge-weighted directed graph have the shortest distances between them. 
In this project, both __imperative__ and __recursive__ solutions were used, and several tests were conducted to determine which function method is more efficient.


## Installation
This project was written in Python language, and its functions can be run using a terminal or any Python-compatible interpreter. Please ensure that ***Pipfile*** is used when installing this project. The ***Pipfile*** incorporated into the new tool 'pipenv' as a handy replacement for the conventional _dependencies_<sup>(or requirements)</sup> file and contains necessary dependancies.


## Unit and Performance testing
In this project, the **'unittest'** module for unit testing and the **'timeit'** module for performance testing were used to compare imperative and recursive functions for the same algorithm. Please note that due to the system state, including Python version and plugins installed, the results may differ slightly from the results below:


#### Unit Test for 'Imperative' function
'''
..
 ----------------------------------------------------------------------
Ran 2 tests in 0.000s
'''


#### Unit Test for 'Recursive' function
'''
..
 ----------------------------------------------------------------------
Ran 2 tests in 0.000s
'''


#### Performance Tests for 'Imperative' and 'Recursive' functions!
'''
***Min*** execution time:
  - imperative:  0.017676700023002923
  - recursive :  0.021591100026853383
***Max*** execution time:
  - imperative:  0.02249970007687807
  - recursive :  0.022994099999777973
***Average*** execution time:
  - imperative:  0.13600709999445826
  - recursive :  0.15710890002083033
 ----------------------------------------------------------------------
'''

Here is an illustration of the test command to run into the terminal:
'''
$ python test_performance.py **OR** $ python test_env/test_floyd_imp.py<sup>this is if you're outside of the ***test_env*** directory</sup>
'''


## Contribution 
If you have any suggestions for how we can better implement these functions, we'd love to hear them.


## Author
'Rashad Gurbanli'