file = open("hello.txt", "w")   #"w" creates a new file, if exists it will replace the existing file
                                #"r" is for reading, "a" is for appending to the file
file.write("Hello, Oweyn!")

file.close()

with open("hello.txt", "w") as file:    # with statement is for automatically close the file even if theres an error

    file.write("Hello!")            

with open("hello.txt", "r") as file:
    content = file.read()
    content = content.strip() # removes any whitespace from the beginning and end of the string, \n
    print(content)
    

text = "Hello,Oweyn!"
result = text.split(",")  # splits the string into a list of substrings based on the comma delimiter
print(result)  # Output: ['Hello', ' Oweyn!']
# it become a list
