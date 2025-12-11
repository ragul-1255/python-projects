import random
answer=random.randint(1,100)
guess=0
score=100
print("guess the number between 1 to 100")
while(True):
    g=input("enter your guess: ")
    if g.isdigit():
        guess=int(g)
        if score!=0:
    
            if guess<1 and guess>100:
                print("its out of range! enter a number between 1 to 100")
                score-=10
                print("your score: ",score)
            elif guess<answer:
                print("its too low!")
                score-=10
                print("your score: ",score)
            elif guess>answer:
                print("its too high!")
                score-=10
                print("your score: ",score)
            else:
                print("CORRECT!")
                print("your score: ",score)
                break
        else:
            print("you are out of points to play")
    else:
        print("enter a number between 1 to 100")
        