age = 20 

print(age> 18)
print(age< 18)
print(age== 20) #Print in bollean (True or False)

#---------------------------------------- #

saving_rate = 15

if saving_rate >30:
    print("Excellent!") # if the statement false, it will not print this line

elif saving_rate > 20:
    print("Good!") # elif statemnt is use for more than two conditions

else:
    print("Keep improving!") # if the statement false, it will print this line

#---------------------------------------- #
  
# Exercise 1 : Ask the user for their exam score
exam_score = float(input("Please enter your exam score:"))
if exam_score >=80:
    print("Excellent!")
elif exam_score >=60:
    print("Pass!")
else:
    print("Study harder...")

# Exercise 2 : Ask the user for their age
age = int(input("Please enter your age:"))
if age >= 18:
    print("Adult")
else:
    print("Minor")

#----------------------------------------- #    

