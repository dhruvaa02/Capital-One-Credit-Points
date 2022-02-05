# Capital-One-Credit-Points

Welcome to my Credit Card Reward Points System program for the Capital One take-home project. 

In this page I will explain what is needed to use my program, how to use it, any assumptions I have made during the creation of the program, how it could be improved, and how this code could be further integrated and scaled.

### Preface

1. I have included both of my implementations as part of this project. My main implementation uses linear algebra/programming to solve the points maximisation. I initially created a brute force implementation which provided to be very beneficial for testing and debugging purposes.
2. Due to my confusion over the description of the "per transaction points rewarded", I decided to print out the maximum points combined with the rules applied as well as how many times the rule was applied. The reason for decision was I was unsure of what was expected from the per transaction points and so I decided to provide what I thought was the most useful information from the rules.

### What's included

- ```main.py```: the main file to be run for my program to be executed. The program will first read a given group of transactions from a JSON formatted file (by default = "transactions.json" in the same directory) before executing my dynamically generated linear programming implementation to calculate the maximum total points, as well as the rules applied and how many times.
- ```rules.py```: file responsible for the rules of the program. Changing the rules in the ```RuleSet``` class will change how the program functions, as well as the apply rule function for the brute force method.
- ```data.py```: file containing the functionality to read from input files, currently reading the monthly transactions and totalling the spendings at each merchant in that month.
- ```brute_force.py```: file containing my first attempt, brute force implementation containing the 2 functions necessary to search through every permutation of rules applied.
- ```lpp_optimizer.py```: this file contains a very hard coded implementation of Google's OR tools in order to solve the exact example provided in the handout. This file is not used in my program, but is incredibly beneficial to understanding how the dynamically generated version works.
- ```dynamic_lpp.py```: my main method. This file generates the necessary equations and to utilize the OR tools in order to maximise the number of rewards points.
- ```transactions.json```: the file containing the transactions for a customer in a given month.

### Prerequisites

- To use and run the program, you need Python 3. As this project was written in Python 3.9.7, for best compatibility, I would recommend upgrading to the latest version of Python 3 if not already done so.

- The most important package in this program is Google's OR tools library. I have included a ```requirements.txt``` file so once the best version of python is installed, install the necessary libraries:

  ```python
  pip install -r requirements.txt 
  ```

  (make sure pip is installed if you run into any errors)

### How to use the program

- Simply run the ```main.py``` file and the program should print the results for the main example in the handout!

- To run the program with other scenarios, there are 2 ways to edit the program: 

  - Change the ```transactions.json``` with different spendings to see different amounts of points for different levels of spending.
  - Add/remove rules from the ```rules``` list from the ```RuleSet``` class in the ```rules.py``` file in the formatted described in the documentation. **Note**: even if there is no 'leftover' points rule, simply change the points provided from leftovers to 0, rather than removing the rule. The first rule should always be the remainder.

- Assuming things went smoothly, you should see an output similar to this:

  ````python
  >>> python3 main.py
  Solution:
  Total points = 1675
  Rule 1: 1 times
  Rule 2: 0 times
  Rule 3: 0 times
  Rule 4: 1 times
  Rule 5: 0 times
  Rule 6: 13 times
  Rule 7: 50 times
  ````

  

### Assumptions

1. The transactions provided in the transactions file is provided in JSON format.
2. The program is run every month, and the transactions file contains the transactions only for one month.
3. The first rule provided in the rules set is always a remainder rule. Even if leftover points are not considered, the amount of points the leftovers return is 0, rather than the rule not existing at all.
4. The transaction amounts are provided in cents, and the rules are determined by dollar basis.
5. The program was allowed to be written in Python.
6. I was allowed to use external libraries, rather than implementing the LPP linear algorithm manually.
7. I was allowed to interchange the per-transaction points for a list of rules and the number of times the rule was applied.

### Improvements and extensions

- 