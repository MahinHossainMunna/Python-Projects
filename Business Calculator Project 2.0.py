'''
Business Calculator
Author : LoneWolf
Date: 20-03-2020
'''

import re

print("Business Calculator 2.0")
print("Type 'quit' or 'q' to exit\n")

previous = 0
run = True

# run math function
def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("0\n")
    else:
        equation = input(str(previous))

    # user when type quit
    if equation == 'quit':
        print("Calculator Shutting Down")
        run = False
    else:
        # to remove all letters of input
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)

        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
