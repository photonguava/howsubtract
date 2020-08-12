import add 
import subtract
import multiply
import divide
import sys

if sys.argv[2] == "+":
    result = add.add(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "-":
    result = subtract.subtract(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "*":
    result = multiply.multiply(sys.argv[1],sys.argv[3])
elif sys.argv[2] == "/":
    result = divide.divide(sys.argv[1],sys.argv[3])

print(result)