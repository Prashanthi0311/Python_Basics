#1. Write a program to print  “Bright IT Career”  ten times using for loop
for i in range(1,11):
    print("Bright IT Career")
    

#2. Write a python program to print 1 to 20 numbers using the while loop.
i=1
while(i<=20):
    print(i,end=" ")
    i+=1
    
    
# 3. Program to equal operator and not equal operators 
a=2
b=3
print('')
print(a==b)  #Equal operator returns false since a and b are not equal
print(a!=b)  #Not equal operator returns true


#4. Write a program to print the odd and even numbers. 
print("Even numbers:")
for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
print("")
print("Odd numbers:")
for i in range(1,21):
    if i%2!=0:
        print(i,end=" ")
print('')
        

#5. Write a program to print largest number among three numbers. 
a,b,c=map(int,input().split())
if a>b and a>c:
    print("Largest Number:",a)
elif b>a and b>c:
    print("Largest Number:",b)
else:
    print("Largest Number:",c)
    
    
#6.Write a  program to print even number between 10 and 20 using while
a=10
b=20
while(a<=b):
    if a%2==0:
        print(a,end=" ")
    a+=1
print()
    

#7.Write a program to print 1 to 10 using the do-while loop statement. 
i=1
while True:
    print(i,end=" ")
    i+=1
    if i>10:
        break#It breaks the loop if the condition becomes false
print()


#8.Write a program to find Armstrong number or not
#Armstrong number-->sum of(each digit^number of digits)==the number itself
num=int(input("Enter a number8:"))
original=num
no_digits=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum+=digit**no_digits
    num//=10
if sum==original:
    print(original,'is an Armstrong number')
else:
    print(original,"is not an Armstrong number")


#9.Write a program to find the prime or not. 
num1=int(input("Enter a number9:"))
if num1<=1:
    print(num1,"is not a prime number")
else:
    for i in range(2,num1):
        if num1%i==0:
            print(num1,"is not a prime number")
            break
    else:
        print(num1,"is a prime number")
        
        
#10. Write a program to palindrome or not. 
num2=int(input("Enter a number10:"))
original=num2
rev=0
while num2>0:
    digit=num2%10
    rev=rev*10+digit
    num2//=10
if rev==original:
    print(original,"is a palindrome")
else:
    print(original,"is not a palindrome")
    
    
#11.Program to check whether a number is EVEN or ODD using switch
num3=int(input("Enter a number11:"))
#we use match insted of switch in python
match num3%2:
    case 0:
        print(num3,"is an even number")
    case 1:
        print(num3,"is an odd number")
    
    
#12.Print gender (Male/Female) program according to given M/F using switch
gender=input("Enter gender(M/F):")
match gender.upper():
    case 'M':
        print('Male')
    case 'F':
        print('Female')