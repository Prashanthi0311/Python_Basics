#1.Write a program to print your name
print("Prashanthi")


#2.Write a program for a single line comment and multi-line comments
#This is a single line comment
print("Single line comment")
'''This is a Multi-line comment
we use three single quotes or double quotes'''
print("Multi-line comment")


#3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a=7
print("type of a:",type(a))
b=False
print("type of b:",type(b))
c='A'
print("type of c:",type(c))
d=1.0
print("type of d:",type(d))
#Double acts as same as float in python


#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables.
a=45#Global variable outside the function
def variable():
    a=50#Local variable inside the function
    print('Local:',a)
variable()
print('Global:',a)