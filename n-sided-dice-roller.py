from random import randint

print("##n-Sided Dice Roller##")
print("The instructions are simple:")
print("\tinput a number greater than 1 (so 2 or more),")
print("\tthe program outputs a random number from 1 to")
print("\tthat number")
print("To quit the program, type 'exit'")
print("....................................")
print("....................................")
print("....................................")

exitLoop = False
while not exitLoop:
    x = input("Please insert a maximum number:")
    if(x == "exit"):
        break
    try:
        x = int(x)
    except ValueError:
        print("Invalid input, please enter a positive integer >1")
        continue
    if(x < 2):
        print("Invalid input, please enter an integer >1")
        continue
    print("...")
    print(randint(1,x))

print("Exiting program, have a nice day! :)")
