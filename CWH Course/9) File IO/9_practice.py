score = int(input("Enter high score: "))

with open("file2.txt","r") as f:
    content = f.read()
    if (content != ""):
        content = int(content)
    else:
        content=0
    print(f"\nPrevious High score: {content}")

    if (score>content):
        with open("file2.txt","w") as f2:
            print("New high score!")
            f2.write(str(score))
    else:
        print("Try Again!!")


with open("file3.txt","r") as f:
    content = f.read()

content = content.lower()

if ("donkey" in content):
    content = content.replace("donkey","######")
    with open("file3.txt","w") as f:
        f.write(content)
    print("\nReplaced successfully.")

else:
    print("\n\"Donkey\" is not in the file.")