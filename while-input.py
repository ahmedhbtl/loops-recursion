# A quick demo of how to use infinite loops to your advantage.
# The code requests input from the user, and continues to loop
# until the user inputs the word "stop".

while True:
    i = input("what is the local sales tax? ")
    if i == "continue":
        print("Looping again...")
    elif i == "stop":
        break
