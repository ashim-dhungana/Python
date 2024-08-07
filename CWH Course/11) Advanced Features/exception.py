def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("This runs no matter the outcome.")

main()


#RAISING EXCEPTION

n1 = int(input("\nEnter number to be divided: "))
n2 = int(input("Enter another number: "))
if (n2==0):
    raise ZeroDivisionError("You cannot divide by zero")
else:
    print(n1/n2)