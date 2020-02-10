Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# string
phrase = input("Enter a string: ")
print("you said " + phrase)
print(f"You said {phrase}")

#float
someFloat = floar(input("Enter a float: "))
print("You entered float: " + str(someFloat))
print("You entered float: {someFloat}")

# int
someInt = float(input("Enter an int: "))
print("You entered int: " + str(someInt))
print("you entered int: {someInt}")

#string interpolation

print (f"Do python inline, like this: {someFloat} * {someInt} + {someFloat * someInt}")
