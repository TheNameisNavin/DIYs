#everyday task
#Nested loops [ 27.5.25 ]

a=0
for i in rnage(2):
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







