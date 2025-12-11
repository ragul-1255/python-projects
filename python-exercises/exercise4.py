import random
import time 
import emoji
options=['r','p','s']
dic={
    "r":emoji.emojize(":rock:"),
    "p":emoji.emojize(":page_facing_up:"),
    "s":emoji.emojize(":scissors:")
}
def inpt():
    while True:
        user=input("enter your choice (r/p/s): ").lower()
        if user not in options:
            print("invalid option")
        else: 
            return user
def disp_choices(user,computer):
     print(f"{'you':<8} : {dic.get(user)}")
     print(f"{'computer':<5} : {dic.get(computer)}")
        
def determine_winner(user,computer):
    if user==computer:
            for i in "MATCH DRAW!\n":
                print(i,end='')
                time.sleep(0.1)
    elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        for i in "YOU WON!\n":
            print(i,end='')
            time.sleep(0.1)
    else:
        for i in "COMPUTER WON!\n":
            print(i,end='')
            time.sleep(0.1)

def play():
    while(True):
        user=inpt()
        computer=random.choice(options)
        disp_choices(user,computer)
        determine_winner(user,computer) 
        wish=input('do you still want to continue(y/n): ').lower()
        if wish == 'y':
            continue
        else:
            break
print('\n')
print("ROCK PAPER AND SCISSORS GAME !".center(50,'*'))
print('\n')
pl=input("shall we start to play(y or n): ").lower()

if pl == 'y':
    play()
else:
    print("ok see you soon!")


    