#CONDITIONAL EXPRESSIONS

age = int(input("Enter your age: "))

if(age>18 and age<100):
    print("You can watch as much porn as you want.")
elif(age==18):
    print("You are 18 years old. Congrats!!")
else:
    print("You cannot watch porn. Get the fuck out!")


m1 = "make money"
m2 = "you won lottery"
message = input("\nEnter your message: ")

if ((m1 in message) or (m2 in message)):
    print("This is a spam")
else:
    print("This is not a spam")

text = input("\nEnter you comment: ")
if ("ashim" in text.lower()):
    print("This post is talking about Ashim")