from curses.ascii import islower
from functools import update_wrapper
from unittest import result


def greet():
    print("hello world !")
var =greet()
print(var)

#Printing factorial using function calling

def factorial(n):
    fact =1
    for i in range (1 ,n+1):
        fact = fact*i
    return fact

fact_of_5 = factorial(5)
print(fact_of_5)

#Printing a table using function calling

def print_table(n):
    for i in range (1,11):
        print(n*i)
print_table(12)

def li():
    ls=[1,2,3]
    return(ls)
var =li()
print(var)



