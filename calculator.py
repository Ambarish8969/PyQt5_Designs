num1 = int(input("Enter a number : "))
num2 = int(input("Enter second number : "))

print(" A is Addition.\n B is Subtraction.\n C is Multiplication.\n D is Division.")

choice = input("Enter your choice A/B/C/D.? : ").lower()

def add(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    subr=num1-num2
    return subr
def mul(num1,num2):
    mult=num1*num2
    return mult
def div(num1,num2):
    divd=num1/num2
    return divd

if choice == "a":
    print(add(num1,num2))
elif(choice == "b"):
    print(sub(num1,num2))
elif(choice == "c"):
    print(mul(num1,num2))
elif(choice == "d"):
    print(div(num1,num2))
else:
    print("Invalid.")
