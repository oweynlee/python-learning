for i in range(5): # Loop run 5 times
    print("Hello")

for i in range(5):
    print(i) # Print 0,1,2,3,4 start from 0 to 4

for i in range(1,6): # Custom range 
    print(i)

for i in range(1,11,2): # Custom range with step, the third one is the step (increment)
    print(i)

count = 1
while count <= 5: # It loop until the condition is false, in this case, it will loop until count is greater than 5
    print(count)
    count += 1 # Increment the count by 1 //  += -> count = count + 1

for i in range (10):
    if i == 5:
        break # Break the loop when i is equal to 5, immediately exit the loop
    print(i)

for i in range(6):
    if i == 3:
        continue # Skip the condition i = 3, print the rest till the loop ends
    print(i)

# ---------------------------------------- #
#Exercise 1: Print numbers from 1 to 20
for i in range (1,21):
    print(i)

#Exercise 2: even numbers from 2 to 20
for i in range (2, 22, 2):
    print(i)

#Exercise 3: input a number
number = int(input("How many times?:"))

for i in range(number):
    print ("Python")




