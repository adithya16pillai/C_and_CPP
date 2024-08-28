# Defines each parameter
ops = {
    "+": (lambda a, b: a+b),
    "-": (lambda a, b: a-b),
    "*": (lambda a, b: a*b),
    "/": (lambda a, b: a/b)
}

#Defines the evalution of a expression
def eval(expression):
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token in ops:
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack.pop()
exp = ""
lens=int(input("Enter no. of elements:  "))
for n in range(lens):
    i=input("Enter one element: ")
    exp+=i
    exp+=" "
print(eval(exp))
#Prints the evaluation of 'exp'