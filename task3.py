#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

import math
num= ""
b= ""
x= ""

while num!= True:
    num= (input("Enter a number: ")).strip()
    q= float(num)
    if q.is_integer():
        if (q % 2)==0:
            print("That is an even integer.")
            break
        else:
            print("That is not an even integer.")
    else:
        print("That is not an even integer")
