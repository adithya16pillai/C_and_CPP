#Take input from the user
x = int(input("Enter a number: ")) 

sum=0

temp = x
while temp>0:
    digit = temp%10
    sum += digit**3 
    temp//=10 

#Display output
if x == sum:
    print(x," is an Armstrong Number.")
else: 
    print(x," is not an Armstrong Number.")
    