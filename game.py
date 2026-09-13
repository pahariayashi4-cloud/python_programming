import random
win,loss=0,0
while True:
    val=random.randint(1,9)
    print("GUESS THE NUMBER AND WIN 5 MILLION")
    user=input("Guess the Number between 1-9 or -1 to Exit the Game: ")
    if user==val:
        print("Yay,u won 5 million")
        win+=1
    elif user!=val:
        print("U are a little retard with ADHD and pansexual whore")
        loss+=1
    else:
        print("U are such a scary dog running from the resposibility like a black man after lotting a bank")
        break
    print("Win: ",win)
    print("Loss: ",loss)