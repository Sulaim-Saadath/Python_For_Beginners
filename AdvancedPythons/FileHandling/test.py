file = open("AdvancedPythons/FileHandling/demo.txt", "r") # Open the file and "r" refers to read the file
# print(file) # Object

# Reads the complete file 
print(file.read()) 

# read the first line
# with open("AdvancedPythons/FileHandling/demo.txt", "r") as f: 
#     l1 = f.readline() # character by character
#     print(l1)

# read the lines of file and returns in list
# with open("AdvancedPythons/FileHandling/demo.txt", "r") as f: 
#     l1 = f.readlines()
#     print(l1)


# with open("AdvancedPythons/FileHandling/demo1.txt", "w") as file:
#     file.write("My name is Sulaim.")

# Too add text inside a file
# with open("AdvancedPythons/FileHandling/demo1.txt", "a") as file:
#     file.write("\nMy name is Saadath.")

# To read and write the file we use r+
with open("AdvancedPythons/FileHandling/demo1.txt", "r+") as file:
    print("Before write",file.read())
    file.seek(7)
    file.write("Hello Python\n")
    
    
    
file.close() # Close the file