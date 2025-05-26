'''
1. Print Numbers from 1 to N (Using for loop) 
Problem: Write a program to print numbers from 1 to N using a for loop. 
● Input: An integer N 
● Output: Numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    print(i+1)


'''
2. Print Even Numbers from 1 to N (Using for loop) Problem: Write a program to print all even numbers from 1 to N using a for loop. 
● Input: An integer N 
● Output: Even numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    if i%2==0:
        print(i)

'''
3. Sum of Numbers from 1 to N (Using for loop) 
Problem: Write a program to find the sum of numbers from 1 to N using a for loop. 
● Input: An integer N 
● Output: Sum of numbers from 1 to N. '''

n=int(input("enter number"))
sum =0
for i in range(n+1):
    sum=sum+i
print(sum)


'''
4. Print Odd Numbers from 1 to N (Using for loop) Problem: Write a program to print all odd numbers from 1 to N using a for loop. 
● Input: An integer N 
● Output: Odd numbers from 1 to N. '''

n=int(input("enter number"))
for i in range(1,n):
    if i%2 !=0:
        print(i)

'''
5. Find Factorial of a Number (Using for loop)
Problem: Write a program to find the factorial of a number using a for loop. 
● Input: An integer N 
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
Problem: Write a program to check if a number is prime using a for loop. 
● Input: An integer N 
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
Problem: Write a program to find the sum of digits of a number using a while loop. 
● Input: An integer n 
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

-----------------------------------------

n= int(input("n:"))

count=0
for i in range(1,n+1):
    if i %3 ==0:
        count+= 1
print(count)

---------------------------------------
n = int(input("n:"))
count=0
for i in range(1, n+1):
    if i%3 == 0:
        count = count+1
print(count)


'''
11. Check if a Number is Palindrome (Using while loop) Problem: Write a program to check if a number is a palindrome using a while loop. 
● Input: An integer n 
● Output: "Palindrome" if the number is a palindrome, "Not Palindrome" otherwise. 
'''

n = int(input())
original = n
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Palindrome" if reverse == original else "Not Palindrome")
---------------------------------------------------------------------------------------
n = int(input("n:"))
a= n
reverse = 0
while n >0:
    reverse = reverse * 10 + n % 10
    n//= 10
print( "Palindrome " if reverse == a else "Not palindrome")


'''
12. Print Multiples of 5 up to N (Using for loop) 
Problem: Write a program to print all multiples of 5 up to N using a for loop. 
● Input: An integer N 
● Output: Multiples of 5 up to N. 
'''

n = int(input("n:"))
for i in range(5,n+1,5):
    print(i)


'''
13. Find the Maximum of Three Numbers (Using for loop) Problem: Write a program to find the maximum of three numbers using a for loop.
● Input: Three integers a, b, c 
● Output: Maximum of a, b, c.
'''

a,b,c = map(int,input().split())
max_num = a
for num in [b,c]:
    if num > max_num:
        max_num = num
print(max_num)


'''
14. Print Reverse of a Number (Using while loop) 
Problem: Write a program to print the reverse of a number using a while loop. 
● Input: An integer n 
● Output: Reverse of n. 
'''

n= int(input("n:"))
reverse = 0
while n>0:
    reverse = reverse * 10 + n%10
    n //= 10
print(reverse)


'''
15. Sum of First N Natural Numbers (Using for loop) 
Problem: Write a program to calculate the sum of the first N natural numbers using a for loop. 
● Input: An integer N 
● Output: Sum of numbers from 1 to N. 
'''
n= int(input("n:"))
sum=0
for i in range(1,n+1):
    sum = sum+i
print(sum)


'''
16. Print Numbers from N to 1 (Using while loop) 
Problem: Write a program to print numbers from N to 1 using a while loop. 
● Input: An integer N 
● Output: Numbers from N to 1. 
'''
n= int(input("n:"))
while n >= 1:
    print(n)
    n = n-1


'''
17. Find Sum of Prime Numbers up to N (Using for loop) 
Problem: Write a program to find the sum of all prime numbers between 1 and N using a for loop.
● Input: An integer N 
● Output: Sum of all prime numbers between 1 and N.
'''

n= int(input("n:"))
total = 0
for num in range(2,n+1):
    is_prime = True
    for i in range(2,int(num ** 0.5)+1):
        if num%i == 0:
           is_prime = False
           break
    if is_prime:
        total = total + num
print(total)


'''
18. Find the Product of Digits of a Number (Using while loop) 
Problem: Write a program to calculate the product of the digits of a number using a while loop. 
● Input: An integer n 
● Output: Product of digits of n.
'''

n= int(input("n:"))
product=1
while n>0:
    product *= n%10
    n//=10
print(product)


'''
19. Print Numbers Divisible by Both 3 and 5 (Using for loop) 
Problem: Write a program to print all numbers divisible by both 3 and 5 up to N using a for loop. 
● Input: An integer N 
● Output: Numbers divisible by both 3 and 5. 
'''

n= int(input("n:"))
for i in range(1, n+1):
    if (i%15 ==0):
        print(i)







