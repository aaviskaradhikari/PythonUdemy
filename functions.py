# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


#simple function
def greet():
    print("This is the first print function")
    print("This the second one")
    print("This the third one")


greet()


#function that allows for input
def greet_with_input(name, age, job):
    print(f"This is the first print function. Your name is {name}")
    print(f"This the second one. You are {age} years old.")
    print(f"This the third one. You work as a {job}")


greet_with_input("Robin", str(21), "Salaryman")


#There are positional arguments and keyword arguments. 

#example of positional:
greet_with_input("Robin", str(21), "Salaryman")

#example of keyword:
greet_with_input(name = "Robin", age = str(21), job = "Salaryman")