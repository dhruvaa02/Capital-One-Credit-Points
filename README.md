# Capital One Credit Card Reward Points System Project

Welcome to my Credit Card Reward Points System program for the Capital One take-home project!

In this page I will explain what is needed to use my program, how to use it, assumptions I made, and how it can be improved, integrated and scaled.

### Preface

1. I have included both of my implementations as part of this project. My main implementation uses linear algebra/programming to solve the points maximization. I initially created a brute force implementation which proved to be very beneficial for testing and debugging.
2. Due to my confusion over the description of the "per transaction points rewarded", I decided to print out the maximum points combined with the rules applied as well as how many times the rule was applied. I was unsure of what was expected from the "per transaction points" so I decided to provide the most useful information from the rules.

### What's included

- ```main.py```: the main file to be run for my program. The program will first read a given group of transactions from a JSON formatted file (by default = "transactions.json" in the same directory) before executing my dynamically generated linear programming implementation to calculate the maximum total points, as well as which rules were applied and how many times.
- ```rules.py```: file responsible for the rules of the program. Changing the rules in the ```RuleSet``` class will change how the program functions, as well as the apply rule function for the brute force method.
- ```data.py```: file containing the functionality to read from input files, currently reading the monthly transactions and totalling the spendings at each merchant in that month.
- ```brute_force.py```: file containing my first attempt, brute force implementation containing the 2 functions necessary to search through every permutation of rules applied.
- ```lpp_optimizer.py```: this file contains a very hard coded implementation of Google's OR tools in order to solve the exact example provided in the handout. This file is not used in my program, but is incredibly beneficial to understanding how the dynamically generated version works.
- ```dynamic_lpp.py```: my main method. This file generates the necessary equations to utilize the OR-tools library in order to maximize the number of reward points.
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

  - Change ```transactions.json``` with different spendings to see different amounts of points for different levels of spending.
  - Add/remove rules from the ```rules``` list in the ```RuleSet``` class. **Note**: even if there is no 'leftover' points rule, simply change the points provided from leftovers to 0, rather than removing the rule. The first rule should always be the remainder.

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

1. The transactions provided in the transactions file are in JSON format.
2. The program is run monthly, and the transactions file contains the transactions only for one month.
3. The first rule provided in the rules set is always a remainder rule. Even if leftover points are not considered, the amount of points the leftovers return is 0, rather than the rule not existing at all.
4. The transaction amounts are provided in cents, and the rules are determined by dollar basis.
5. The program was allowed to be written in Python.
6. I was allowed to use external libraries, rather than implementing the LPP linear algorithm manually.
7. I was allowed to interchange the per-transaction points for a list of rules and the number of times the rule was applied.

### Scalability, improvements & extensions

- Scalability:
  1. The program dynamically generates its rules. Thus, no matter how many rules you give the program, or how large the number of transactions given are, the program will maximize the rewards points.
  2. The program doesn't just brute force the solution, therefore as it is mainly just linear algebra, this solution should be far quicker and more efficient for larger sized inputs.
  3. The program prints to standard output, so outputs could be saved to files and saved in databases easily rather than returning and hence is overall more compatible.
- Improvements that can be made:
  1. The rules could be input through a file rather than having to edit the ```rules.py``` file directly.
  2. Much better error handling could be implemented, rather than simple if checks followed by print statements.
  2. There is a certain level of coupling. The project could be designed better to better conform to SOLID and clean architecture principles.
- Extensions:
  1. The choice of algorithm could be given to the user of the program, rather than being a hard coded choice.
  2. The entire program could be run with command line arguments, and then perhaps with a frontend UI.
  3. The program could be hosted on some platform to make it more accessible, without the need of installing Python and other dependencies locally.

If you have any questions, please feel free to reach out to me at: dhruvaa.saravanan@gmail.com

I look forward to meeting you!
