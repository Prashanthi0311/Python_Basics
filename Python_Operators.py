#1. Write a function for arithmetic operators(+,-,*,/) 
def arithmetic(a,b):
    print(a+b,a-b,a*b,a/b)
arithmetic(20,10)


#2.Write a method for increment and decrement operators(++, --)
def increment(num):
    return num+1
def decrement(num):
    return num-1
num=10
print("Original value:",num)
print("After increment:",increment(num))
print("After Decrement:",decrement(num))


#3. Write a program to find the two numbers equal or not. 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a==b:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")
    

#4. Program for relational operators (<,<==, >, >==)
a=5
b=10
print(a>b)#Prints false as a is less than b
print(a>=b)#Prints false a is less than b and not equal to b
print(a==b)#prints false as a is not equal to b
print(a<b)#prints true as a is less than b
print(a<=b)#prints true as a is less than b
print(a!=b)#prints true as a is not eaual to b


#5. Print the smaller and larger number 
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    print("Larger number:",num1)
    print("Smaller number:",num2)
elif num1<num2:
    print("Larger number:",num2)
    print("Smaller number:",num1)
else:
    print("Both are equal")