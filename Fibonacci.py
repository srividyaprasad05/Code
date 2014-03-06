#! /usr/bin/python

numbers=raw_input("How many numbers would you like to display :")
a=1
b=1
print a
print b

for d in range(int(numbers)):
    
    print " Value of d: " , d
    c=a+b
    print c
    a=b
    b=c

print "All the Fibonacci Series is printed."   




