# Python programming fundamentals

## Console communication
In Computer science learning the basic conctepts and basic logic starts simple - simple for a computer is the console. When initially software developers needed to find a way to communicate with the PC, they came up with the console, where by running different commands, the computer started to prompt the user for different input based on the program's realization. 

The two basic Python 3 commands for input and output of the console are:
``` Python
input()
print()
```

## Data types
* Boolean​
* Numeric​
* String​
* Sequence​
* Dictionary​
* Set

## Operators
* Logical: &&, ||, is, not​
* Arithmetic: +, -, *, /, %, **, //​
* Bitwise: |, &, ^, <<, >>, ~​
* Assignment: =, +=, -=, *=, /=, %=, **=, //=, &=, |=. ^=, <<=. >>=​
* Comparison: ==, !=, <, >, <=, >=

## Conditions
In Python there are 2 ways to manipulate logic based on conditions: *if* and *match*:

``` Python
a = 5
if a == 10:
    print("a is 10")
elif a > 10:
    print("a is more than 10")
else:
    print("a is less than 10")
```

``` Python
a = 5

match a:
    case 1:
        print("a is 1")
    case 5:
        print("a is 5")
    case 10:
        print("a is 10")
    case _:
        print("a is not recognized as a valid option")
```