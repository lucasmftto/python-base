__version__ = "0.1.0"
__author__ = "Lucas FAvaretto"
__license__ = "Unlicense"

import os
import sys

args = sys.argv[1:]
operators = {"sum": None, "sub": None, "mul": None, "div": None}
operator = None
numberOne: float
numberTwo: float

# print(sys.argv)
# print(sys.argv[1])

if not args:
    operator = input("Operação:")
    numberOne = input("n1:")
    numberTwo = input("n1:")
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

numberOne, numberTwo = validated_nums

# print(numberTwo)

if operator == "sum":
    result = numberOne + numberTwo

elif operator == "sub":
    result = numberOne - numberTwo

elif operator == "mul":
    result = numberOne * numberTwo

elif operator == "div":
    result = numberOne / numberTwo
    
# print(result)
print(f"Result is: {result}")
    
