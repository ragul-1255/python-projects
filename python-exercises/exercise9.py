import random
import time
def spin(symbols):
        row=[random.choice(symbols) for i in range(3)]
        print('| ',end='')
        for i in row:
            print(i,end=' | ')
            time.sleep(0.2)
        return row
def result(row):
        if row[0]==row[1] and row[1]==row[2]:
            print("you won $10!")
            return 10
        else:
            print("you lost!")
            return 0
def main():
    balance=100
    symbols=['🍊','🍋','🍉']
    print("*"*20)
    print("Welcome to Python Slots")
    print("Symbols: ",symbols)
    print("*"*20)
    print("\n")
    while True:
        print('your current balance:$',balance)
        while balance>0:
            bet=input("enter your bet amount:$")
            if not bet.isdigit():
                print("enter a valid amount")
                continue                                       
            elif int(bet)<=0:
                print("bet amount can't be negative or zero")
                continue     
            elif int(bet)>balance:
                print("your don't have that much balance to bet")                                        
            else:
                balance-=int(bet)
                break
        else:
            print("you don't have sufficient amount to play")
            break
        print("spinning",end='')
        for i in '.....':
            print(i,end='')
            time.sleep(0.2)
        print('\n****************')
        r=spin(symbols)
        print('\n****************')
        balance+=result(r)
        
        play=input("do you want to continue playing(y/n): ").lower()
        if play=='y':
            continue
        elif play=='n':
            print("*"*25)
            print("your current balance:$",balance)
            print("*"*25)
            break
if __name__=='__main__':
     main()