# Create a variable of each type: string, integer, float, and boolean. Print their types using type().
# str="jitu"
# int=29
# float=24.62
# bool=True
# print(type(str))
# print((type(int)))
# print(type(float))
# print(type(bool))



# Convert a float value to an integer, and then to a string. Show the output at each step.
# my_float=24.62
# my_int=int(my_float)
# my_str=str(my_int)
# print(my_int)
# print(my_str)
# print(type(my_str))


# Use an f-string to display: "Hello <name>, you are <age> years old".
# name="jitendra"
# age=29
# print(f"hello {name}, you are {age} years old")


# Make a list with at least 5 items of different data types. Access and print the second item.
# list=[5,5.2,"five",True,[1,2,3]]
# print("the second element is", list[1])

# Add a new element to a list using .append() and then remove the last element using .pop().
# my_list=[1,2,3,4]
# my_list.append(6)
# print(my_list)
# my_list.pop(2)
# print(my_list)


# Reverse a list using .reverse() and print it.
# my_list=[1,2,3,4]
# my_list.reverse()
# print(my_list)


# Create a dictionary with 3 key–value pairs and print only its keys.
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai"
}

print("Keys of the dictionary:", my_dict.keys())




# Given two lists keys = ["id", "name", "age"] and values = [101, "Aman", 25], create a dictionary using zip() and print it

keys = ["id", "name", "age"]
values = [101, "jitendra", 29]

# Creating dictionary using zip()
my_dict = dict(zip(keys, values))

# Printing the dictionary
print("Created dictionary:", my_dict)
