import os.path
f=input("input the filename: ")
extension = os.path.splitext(f)[1]
print("The extension of the file is: "+extension)
