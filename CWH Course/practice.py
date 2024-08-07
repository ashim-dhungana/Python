n = int(input("Enter number: "))

def recur(n):
    if (n==0):
        return ("")
    print("*"*n)
    return recur(n-1)

draw = recur(n)