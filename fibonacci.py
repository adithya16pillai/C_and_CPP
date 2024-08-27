#Take input from the user
n= int(input(""))
x,y = 0,1 
count = 0

if n<=0:
    print("Enter a positive number")
elif n==1:
    print("The sequence upto", n, ":")
    print(x)
else: 
    print("The Fibonacci Sequence : ")
    while count< n:
        print(x)
        z=x+y
        x=y
        y=z
        count +=1
