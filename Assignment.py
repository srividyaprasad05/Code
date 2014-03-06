import sys

#Total Number of Args

total=len(sys.argv)

#Get args List

cmdargs=str(sys.argv)

a=sys.argv[1]
b=sys.argv[2]


print("Total Number of Args passed: %d " %total)
print("Args list : %s" %cmdargs)

print a
print b

print int(a)*int(a)+int(b)*int(b)+2*int(a)*int(b)
print int(a)*int(a)+int(b)*int(b)-2*int(a)*int(b) 
print int(a)*int(a)-int(b)*int(b)



Command Line Input:

python Assignment.py 10 5

Answers:

225
25
75
