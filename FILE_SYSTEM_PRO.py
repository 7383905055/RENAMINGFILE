import os

from_dir = "C:/Users/rizho/OneDrive/Desktop/WHITEHAT/sample doc/white.txt"
to_dir = "C:/Users/rizho/OneDrive/Desktop/WHITEHAT/sample doc/new.txt"

os.rename(from_dir,to_dir)
print("YOUR FILE HAS RENAMED FROM SOURCE TO DESTINATION NAME!!!")