"""
On initiation, a random integer between 1 and 20 will be generated, and 
based off the random number, we will check its category.
if the number is greater than 15, then the results will be "Cherries"
otherwise if the number is > 10, then the result will be "Orange"
otherwise if the number is > 5, then the result will be "Plum"
otherwise if the number is > 2, then the result will be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
if the number is not any of the above, then the result will be "Bar"
a loop will go over three times and print the results to the user.

"""

"""
import  random
num = generate random number
if num is greater than 15, 
    then the results will be "Cherries"
otherwise if the number is > 10, 
    then the result will be "Orange"
otherwise if the number is > 5, 
    then the result will be "Plum"
otherwise if the number is > 2, 
    then the result will be "Melon"
otherwise if the number is > 1, 
    then the result will be "Bell"
otherwise 
    the result will be "bar"
loop three times
    print the output (fruit) to the user

"""
import random

def main():
    for i in range(0, 3):
        spin()

def spin():
    rand_num = random.randint(1,20)
    output = ""
    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output ="Orange"
    elif(rand_num > 5):
        output ="Plum"
    elif(rand_num > 2):
        output ="Melon"
    elif(rand_num > 1):
        output ="Bell"
    else: 
        output = "Bar"

    print(output, end=" ")

main()