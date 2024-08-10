import os

# Displaying Content
directory_path = "."
contents = os.listdir(directory_path)
for i in contents:
    print(i)
    

# Environment Variables
home_dir = os.environ.get("HOME")
print(f"Home directory: {home_dir}")

print(os.environ["SHELL"])
os.environ["MY_VARIABLE"] = "Ashim The King"
print(f"MY_VARIABLE: {os.environ['MY_VARIABLE']}")


# Process Management
command = "ls -l"
os.system(command)


# Information Retrieval
os_name = os.name
cwd = os.getcwd()
uid = os.getuid()
print(f"Operating System: {os_name}")
print(f"Current Working Directory: {cwd}")
print(f"User ID: {uid}")