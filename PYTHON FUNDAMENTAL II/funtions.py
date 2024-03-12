# functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - Optimizes and make a block of code reusable.

# void function
def averageOfThreeNumbers(num1, num2, num3):
    #codes ...
    average = (num1 + num2 + num3) / 3
    print("Average: ", average)

#SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE: alt + shigt + ArrowDown/ArrowUp

averageOfThreeNumbers(89, 76, 81)
averageOfThreeNumbers(89, 76, 81)
averageOfThreeNumbers(89, 76, 81)

# return function
title = "ang alamat ni Loudie"  
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def StringToUppercase(message):
    return message.upper()

def StringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(StringToUppercase(title))
print(StringToLowercase(title))
# print(joinString(title, title2))
print(countLetters(title))