#using normal method

Syntax: 
a=input()
b=input()
print("the value is", a ,b)

I/P: 
10
20

O/P: 
the value is 10 20

#usinf string modulo operator
Syntax:
x=input()
y=input()`
print("the values are %d%d" % (x,y))

I/P:
10
20

O/P:
the values are 1020


#using F-format method

Syntax : print("{}{}....".format(variable1, variable2,..))
Example:
I/P:

x = 10
y = 20
print(f'the values are {x}{y})

O/P:
the values are 1020


#using dot format method

Example:

I/P:
a = 2.4567
b= 20
print(" the values are {:.4f} and {}".format(a,b))

O/P:  the values are 2.4567 and 20
