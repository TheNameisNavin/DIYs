#everyday task
#Nested loops [ 27.5.25 ]

a=0
for i in range(2):
  for i in range(1,4):
    print(a,end="")
  print()
  a+=1

O/P: 
000
111

#to print pattern -1 

rows=6
for i in rnage(rows):
  for j in range(i):
    print(i, end= " ")
  print()

O/P:
1
22
333
4444
55555

#to print pyramid patterns of numbers

rows=7
for i in range(1,rows+1):
  for j in range(1, i+1):
    print(j, end="")
  print("")

O/P:
1
12
123
1234
12345
123456
1234567

#Pattern - 1

O/P:'''
* * *
* * *
* * *
'''
#Approach - 1 [for inside For]

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()

#Approach - 2 [For inside While]
#Outer -> while
#Inner -> For

temp = 0
while temp <= 2:
    for i in range(3):
        print("*",end=" ")
    print()
    temp = temp + 1

#Approach - 3 [While inside For]
#Outer -> For
#Inner -> While

for x in range(3):
    y = 0
    while y <= 2:
        print("*",end=" ")
        y = y + 1
    print()

#Approach - 4 [While inside While]
#Outer -> while
#Inner -> While

x = 0
while x <= 2:
    y = 0
    while y <= 2:
        print("*",end=" ")
        y = y + 1
    print()
    x = x  + 1

#Approach - 5 [Single for]

for i in range(3):
    print("* "*3)

#Pattern - 2
O/P:

101 102 103
104 105 106
107 108 109

#Approach - 1 [For inside For]

temp = 101
for i in range(3):
    for j in range(3):
        print(f"{temp}",end=" ")
        temp = temp + 1
    print()

O/P:

1 2 3
4 5 6
7 8 9

#Approach - 2 [For in For]

temp = 100
for i in range(3):
    for j in range(3):
        print(f"{temp+1}",end=" ")
        temp = temp + 1
    print()

#Pattern - 3
O/P:

#
# #
# # #
# # # #

#Approach - 1 [For in For]

for i in range(4):
    for j in range(4):
        if i>=j:
            print("#",end=" ")
    print()

#Approach - 2

for i in range(4):
    print("# "*(i+1))

#Pattern - 3
O/P:

# # # #
#     #
#     #
# # # #

#Approach - 1

for i in range(4):
    for j in range(4):
        if i==0 or j==0 or i==3 or j==3:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

#Pattern - 4

O/P:
'''
n=4
1 1 1 1
$ $ $ $
2 2 2 2
$ $ $ $
'''

n = 5
1 1 1 1 1
$ $ $ $ $
2 2 2 2 2
$ $ $ $ $
3 3 3 3 3
'''
#Approach - 1
'''
n = int(input())
temp = 1
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(f"{temp}",end=" ")
        temp = temp + 1
    else:
        for j in range(n):
            print("$",end=" ")
    print()
'''
#Pattern - 5

O/P:
'''
n = 5
$ $ $ $ $
1 2 3 4 5
$ $ $ $ $
1 2 3 4 5
$ $ $ $ $
'''
#Approach - 1
'''
n = int(input())
for i in range(n):
    if i%2==0:
        for j in range(n):
            print("$",end=" ")
    else:
        temp = 1
        for j in range(n):
            print(f"{temp}",end= " ")
            temp = temp + 1
    print()
'''
#Approach - 2
'''
n = int(input())
for i in range(n):
    if i%2==0:
        for j in range(n):
            print("$",end=" ")
    else:
        for j in range(n):
            print(f"{j+1}",end= " ")
    print()
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

'
ATM
Pooja would like to withdraw X US Dollar from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 US Dollar.

Calculate Pooja's account balance after an attempted transaction.

Input Format
Each input contains 2 numbers 
X and Y.
X is the amount of cash which Pooja wishes to withdraw.
Y is Pooja's initial account balance.

Output Format
Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

Constraints
0<X≤2000 - the amount of cash which Pooja wishes to withdraw.

0≤Y≤2000 with two digits of precision - Pooja's initial account balance.
'''

Code: 

# cook your dish here
x,y = map(float,input().split())
if x%5 == 0 and y >= (x+0.5):
    y=y-(x+0.50)
    print(y)
else:
    print(y)

-------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Sum OR Difference
Write a program to take two numbers as input and print their difference if the first number is greater than the second number 

otherwise print their sum.

Input Format
First line will contain two numbers, 

(N1) and (N2), separated by a space.

Output Format
Output a single line containing the difference of 2 numbers 
(N1−N2) if the first number is greater than the second number otherwise output their sum 
(N1+N2).

Constraints

−1000≤N1≤1000

−1000≤N2≤1000
'''

Code:
# cook your dish here
x, y=map(int,input().split())
if x>y:
    print(x-y)
else:
    print(x+y)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Volume Control
Chef is watching TV. The current volume of the TV is X. Pressing the volume up button of the TV remote increases the volume by 
1 while pressing the volume down button decreases the volume by 1. Chef wants to change the volume from X to Y. Find the minimum number of button presses required to do so.

Input Format
The first line contains a single integer 
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
X and Y - the initial volume and final volume of the TV.

Output Format
For each test case, output the minimum number of times Chef has to press a button to change the volume from X to Y.

Constraints

1≤T≤100
1≤X,Y≤100
'''
Code:

# cook your dish here
t=int(input())
for _ in range(t):
    x,y= map(int,input().split())
    if x>y:
        print(x-y)
    else:
        print(y-x)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Reach on Time
Chef has recently moved into an apartment. It takes 
30
30 minutes for Chef to reach office from the apartment.

Chef left for the office 
X
X minutes before Chef was supposed to reach. Determine whether or not Chef will be able to reach on time.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single integer 
X
X.
Output Format
For each test case, output YES if Chef will reach on time, NO otherwise.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

Constraints
1
≤
T
≤
60
1≤T≤60
1
≤
X
≤
60
1≤X≤60
'''

Code:

# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    if x >= 30 :
        print("YES")
    else:
        print("NO")

--------------------------------------------------------------------
'''
Maximum Submissions
A participant can make 
1
1 submission every 
30
30 seconds. If a contest lasts for 
X
X minutes, what is the maximum number of submissions that the participant can make during it?

It is also given that the participant cannot make any submission in the last 
5
5 seconds of the contest.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single integer 
X
X, denoting the number of minutes.
Output Format
For each test case, output the maximum number of submissions a participant can make in 
X
X minutes.

Constraints
1
≤
T
≤
30
1≤T≤30
1
≤
X
≤
30
1≤X≤30
'''

Code:

# cook your dish here
t = int(input())
for _ in range(t):
    x= int(input())
    y = 2*x
    print(y)
