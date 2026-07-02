student = {"name": "Oweyn", 
           "age": 20, 
           "dream_company": "JPMorgan" 
           }
print(student) # This will print the whole dictionary.
print(student["name"]) # This is call key, instead of list uses numbers to access values.
print(student["age"]) 
print(student["dream_company"]) 


#If i type the key that does not exist, it will return an error, "KeyError", unlike lists that will return "IndexError" if the index does not exist.

person = {
    "name": "Oweyn",
    "age": 19,
    "country": "Malaysia"
}

for key in person:  # Print the keys in the dictionary, which are "name", "age", and "country"
    print(key)      #Trear it as the keys are the drawers, and the values are the items in the drawers.
    #in loops, key is just a string

for key in person:
    print(person[key]) # Print the values in the dictionary, which are "Oweyn", 19, and "Malaysia"

# ---------------------------------- #

expenses = []

expense = {
    "category": "Food",
    "amount": 20
}

expenses.append(expense)

print(expenses)



# U