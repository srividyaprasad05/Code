import sys

#Total Number of Args

total = len(sys.argv)

#Get Args List

cmdargs = str(sys.argv)

a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]

print("Total Number of Args Passed to the script: %d " % total)
print("Args List: %s " % cmdargs)

print a
print b
print c

print int(a)+int(b)+int(c)


