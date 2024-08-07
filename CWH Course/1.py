#INTRO

print("Hello World")

print('''I am Ashim,
I am a fucking legend
and I am God's favorite''')


# Displaying the content of directory

import os

directory_path = '/run/media/ashim/Programming/Python/Course/'
contents = os.listdir(directory_path)

print("\nHere are the items in this folder:")
for item in contents:
    print(item)