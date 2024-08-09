import shutil
import os
import time

shutil.copy("shutil_module.py","shutil_module2.py")
print("Creating copy...")

time.sleep(3)

# os.remove("shutil.py")
# print("Deleting copy...")

# time.sleep(3)

# shutil.copy2("shutil_module.py","shutil2.py")
# print("Creating advanced copy...")