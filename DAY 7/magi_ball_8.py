import random
import sys
message=["It is certain", "It is decidedly so", "Without a doubt", "Yes – definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes Signs point to yes", "Reply hazy", "try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def play():
    x=input("Ask your question here : ")
    print(message[random.randint(0,len(message)-1)])
    replay()

def replay():
    y=input("You want to ask another question [y/n] : ")
    if(y=="y" or y=="Y"):
        play()
    elif y == 'N' or y=='n':
        try:
            sys.exit()
        except:
            print("Exit")
    else:
        print('I apologies, I did not catch that. Please repeat.')
        replay()

play()

# print("Hello")