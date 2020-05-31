import random
print("This is a number guessing game. You will be getting FIVE chances to guess the correct number. Are you ready ? ")
secret = random.randint(1,20)
for i in range(5):
    guess=int(input("Guess a number between 1 and 20 : "))
    if(i==4):
        print("Sorry !! You reached the maximum limit")
        print("Better luck next time")
    elif(guess==secret):
        print("You guessed the correct number")
        print("You guessed the correct answer in "+ str(i+1) + " attemps")
        print("Thanx for playing..")
        break
    elif(guess<secret): 
        print("Your guess is lower than my number")
    else:
        print("Your guess is higher than my number")
