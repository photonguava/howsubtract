#import add 
#import subtract
#import multiply
#import divide
import sys

if sys.argv[2] == "+":
    add.add(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "-":
    subtract.subtract(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "*":
    multiply.multiply(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "/":
    divide.divide(sys.argv[1],sys.argv[3])