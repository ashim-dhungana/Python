#FUNCIONS

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

def avg(a,b):
    average = (a+b)/2
    print(average)

    return "Done"

return_value = avg(a,b)
print(return_value)


#Recursive function

def factorial(n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)

num = int(input("Enter number whose factorial is needed: "))
ans = factorial(num)

print(f"Factorial of {num} = {ans}")