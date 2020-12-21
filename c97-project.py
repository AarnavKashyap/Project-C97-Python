import random

print("Number Guessing Game");
print("Guess a number between 1 - 9");

randomNumber = random.randrange(1,9)
count = 5

while count > 0:
    number = int(input("Enter your guess:- "))
    if number == randomNumber:
        print("Congratulations you won!")
        break
    elif number < randomNumber:
        print("Your guess is too low! Try a number greater than " + str(number))
    elif number > randomNumber:
        print("Your guess is too high! Try a number lesser than " + str(number))

    count -= 1

if count == 0:
    print("You Lose!")
