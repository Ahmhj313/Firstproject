#Everyone knows the story of the first line
print("Hello world!")
print("")
#Tells you what this is all about
print("This is an x/y function program")

#Tells you what to write as an x value for the division
print("Insert your x value")
x = input()

#Tells you what to write as an y value for the division
print("Now insert your y value")
y = input()

#Converts our values to integers
x = int(x)
y = int(y)

#Does the divion
z = x/y
#Converts our integer into a string so we can put it in a sentence
print("Your result is = " + str(z))
