#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os
import sys

from datetime import datetime

args = sys.argv[1:]
operators = {"sum": None, "sub": None, "mul": None, "div": None}
operator = None
numberOne: float
numberTwo: float

validated_operations = {
    "sum": lambda n1, n2: n1 + n2,
    "sub": lambda n1, n2: n1 - n2,
    "mul": lambda n1, n2: n1 * n2,
    "div": lambda n1, n2: n1 / n2,
}
# print(sys.argv)
# print(sys.argv[1])

if not args:
    operator = input("Operação:")
    numberOne = input("n1:")
    numberTwo = input("n2:")
    args = [operator, numberOne, numberTwo]
elif len(sys.argv[1:]) != 3:
    print("Argumentos invalidos!")
    sys.exit(1)

operator, *nums = args

if operator not in operators:
    print(f"Invalid Option `sys.argv[1]`")
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Invalid Number {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    numberOne, numberTwo = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)

# print(numberTwo)

result = validated_operations[operator](numberOne, numberTwo)


path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

# print(result)
print(f"Result is: {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operator}, {numberOne}, {numberTwo} = {result}\n")
except PermissionError as e:
    print(str(e))
    sys.exit(1)      
    

    
