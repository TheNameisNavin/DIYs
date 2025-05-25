'''
1. Print Numbers from 1 to N (Using for loop) 
Problem: Write a program to print numbers from 1 to N using a for loop. ● Input: An integer N 
● Output: Numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    print(i+1)


'''
2. Print Even Numbers from 1 to N (Using for loop) Problem: Write a program to print all even numbers from 1 to N using a for loop. ● Input: An integer N 
● Output: Even numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    if i%2==0:
        print(i)

'''
3. Sum of Numbers from 1 to N (Using for loop) 
Problem: Write a program to find the sum of numbers from 1 to N using a for loop. ● Input: An integer N 
● Output: Sum of numbers from 1 to N. '''

n=int(input("enter number"))
sum =0
for i in range(n+1):
    sum=sum+i
print(sum)


'''
4. Print Odd Numbers from 1 to N (Using for loop) Problem: Write a program to print all odd numbers from 1 to N using a for loop. ● Input: An integer N 
● Output: Odd numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    if i%2 !=0:
        print(i)

'''
5. Find Factorial of a Number (Using for loop)
Problem: Write a program to find the factorial of a number using a for loop. ● Input: An integer N 
● Output: Factorial of N. 
'''

n=int(input("enter number"))
f=1
for i in range(1,n+1):
    f = f*i
print(f)

'''
6. Print Multiplication Table of N (Using for loop) 
Problem: Write a program to print the multiplication table of a number N (up to 10) using a for loop. 
● Input: An integer N 
● Output: Multiplication table of N. 
'''

n=int(input("enter the number"))
for i in range(1,11):
    print("%d * %d = %d" % (n , i , n*i))

'''
7. Check Prime Number (Using for loop) 
Problem: Write a program to check if a number is prime using a for loop. ● Input: An integer N 
● Output: "Prime" if the number is prime, "Not Prime" otherwise. 
'''
n = int(input("n:"))
is_prime = True

if (n < 2):
    is_prime = False
else:
    for i in range( 2, int(n** 0.5 )+ 1):
        if n%i == 0:
           is_prime = False
           break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

'''
8. Sum of Digits of a Number (Using while loop) 
Problem: Write a program to find the sum of digits of a number using a while loop. ● Input: An integer n 
● Output: Sum of the digits of n. 
'''

n = int(input("n:"))
sum = 0
while n > 0:
    sum += n%10
    n //= 10
print(sum)

'''
9. Print Fibonacci Sequence un= p to N Terms (Using for loop) Problem: Write a program to print the Fibonacci sequence up to N terms using a for loop.
● Input: An integer N 
● Output: Fibonacci sequence up to N terms. 
'''

n = int(input("n:"))
a,b =0,1
for i in range(n):
    print(a, end="")
    a,b = b, a+b

'''
10. Count Numbers Divisible by 3 (Using for loop) 
Problem: Write a program to count how many numbers between 1 and N are divisible by 3 using a for loop. 
● Input: An integer N 
● Output: Count of numbers divisible by 3. 
'''

n = int(input("n:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count = count + 1
print(count)
