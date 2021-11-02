import random

lower_number = input("Lower Number : ")
upper_number = input("Upper Number : ")

#Bottom Number
if lower_number.isdigit():
    lower_number = int(lower_number)
elif lower_number.isdigit() <= 0:
    lower_number = int(lower_number)
else:
    quit()

#Top Number
if upper_number.isdigit():
    upper_number = int(upper_number)
elif upper_number.isdigit() <= 0:
    upper_number = int(upper_number)
else:
    quit()


random_number = random.randint(lower_number,upper_number)
guess = 0

guesses = True

while guesses:
    guess += 1
    guess_number = input("Make a Guess Number : ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please Type a Number")
        continue
    
    if guess_number == random_number:
        print("You got it!")
        break
    else:
        print("Try Again")

print("You guess",guess,"times")