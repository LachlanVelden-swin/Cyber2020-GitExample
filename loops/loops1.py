# Write a program that totals every number between 10 and 50, and outputs the subtotal on a separate line.

# Write a program asks for names and adds the name to an existing sentence until an empty name is entered, then oututs all of the names within that sentence.
# GoalSentence = "Hello bob, fred, george, how are you?"


name = None
listOfNames = ""

while (name != ""):
    name = input("What is a name? ")
    if(name != ""):
        listOfNames = listOfNames + name + ", "
        print(listOfNames)

print("Hello " + listOfNames + "how are you?")