try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

    #If the file doesn't exist, it will print "File not found" instead of crashing
